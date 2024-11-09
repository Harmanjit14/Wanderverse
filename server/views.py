from django.conf import settings
from django.shortcuts import redirect, render
from django.core.signing import BadSignature
from django.core import signing
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django_ratelimit.decorators import ratelimit
from leaderboard.models import Leaderboard
from server.forms import AnswerForm, StartGameForm
from .geminiMethods import getQUIZ, validateQUIZ
import uuid


def get_signed_data(data):
    """Helper function to safely decode signed data."""
    try:
        return signing.loads(data)
    except BadSignature:
        return None


def homepage(request):
    """Home page view where the game starts and score is initialized."""
    signed_score = request.GET.get("score")
    signed_score = signing.dumps(0)  # Reset score at the start
    form = StartGameForm()

    leaderboard_data = Leaderboard.objects.all()
    gcp_key = settings.GCP_MAPS_KEY

    return render(
        request,
        "homepage.html",
        {
            "form": form,
            "score": signed_score,
            "leaderboard_entries": leaderboard_data,
            "gcp_key": gcp_key,
        },
    )


@csrf_protect
@ratelimit(key="ip", rate="5/m", method="POST", block=True)
def leaderboard(request):
    """Handle submission of username and score to the leaderboard."""
    if request.method == "POST":
        signed_score = request.POST.get("score")
        username = request.POST.get("answer")
        submission_id = request.POST.get("submission_id")

        # Check if required fields are present
        if not username or not signed_score:
            messages.error(request, "Missing username or score data.")
            return redirect("home")

        if submission_id != request.session.get("submission_id"):
            messages.error(request, "Invalid or reused submission ID.")
            return redirect("home")
        # Ensure the UUID can only be used once
        if "used_submission_ids" not in request.session:
            request.session["used_submission_ids"] = []

        if submission_id in request.session["used_submission_ids"]:
            messages.error(request, "Duplicate submission detected.")
            return redirect("home")

        # Validate signed score
        score = get_signed_data(signed_score)
        if score is None:
            messages.error(request, "Invalid score data.")
            return redirect("home")

        # Insert score and username into the leaderboard database here
        Leaderboard.objects.create(user=username, score=score)
        request.session["used_submission_ids"].append(submission_id)
        del request.session["submission_id"]
    return redirect("home")


@csrf_protect
def result(request):
    """Process and validate the user's quiz answer."""
    if request.method == "POST":
        form = AnswerForm(request.POST)
        signed_score = request.POST.get("score")
        signed_city = request.POST.get("city")

        # Verify score and city data
        score = get_signed_data(signed_score) or 0
        city = get_signed_data(signed_city) or "Unknown Location"

        if form.is_valid():
            answer = form.cleaned_data["answer"]

            # Validate quiz answer
            response = validateQUIZ.validateQuiz(answer, city)
            if response is None:
                messages.error(request, "Failed to validate game result. Try again.")
                return redirect("home")

            score += response
            signed_score = signing.dumps(score)
            submission_id = str(uuid.uuid4())
            request.session["submission_id"] = submission_id

            # Set failure/success response based on answer
            template = "failure.html" if response <= 1 else "success.html"
            context = {
                "score": signed_score,
                "totalScore": score,
                "gain": response,
                "city": city,
                "user_city": answer,
                "submission_id": submission_id,
            }
            return render(request, template, context)

    messages.error(request, "Invalid form submission.")
    return redirect("home")


@csrf_protect
def playGame(request):
    """Start or continue the game with a new quiz question."""
    if request.method == "POST":
        signed_score = request.POST.get("score")
        score = get_signed_data(signed_score) or 0

        # Update the score
        score += 1
        signed_score = signing.dumps(score)

        # Fetch a random quiz question
        quiz_data = getQUIZ.getRandomQuiz()
        if not quiz_data:
            messages.error(request, "Failed to load game data. Try again.")
            return redirect("home")

        location = quiz_data.get("location", {})
        city = location.get("location_name", "Unknown Location")
        signed_city = signing.dumps(city)
        gcp_key = settings.GCP_MAPS_KEY

        # Prepare game context
        context = {
            "range": 2000,
            "roll": 0,
            "heading": 90,
            "tilt": 60,
            "history": quiz_data.get("context"),
            "hints": quiz_data.get("hints"),
            "latitude": float(location.get("latitude", 0.0)),
            "longitude": float(location.get("longitude", 0.0)),
            "score": signed_score,
            "form": AnswerForm(),
            "city": signed_city,
            "gcp_key": gcp_key,
        }
        return render(request, "game.html", context)

    messages.error(request, "Invalid request method.")
    return redirect("home")
