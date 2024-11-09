import google.generativeai as genai
from ..API.constants import scoreFormat, scoreResponseFormat
import json


def validateQuiz(user_guess, correct_answer):
    # Refine query for Gemini API to specify type of response requested
    # Prepare the query for the Gemini API
    query_template = scoreFormat
    refined_query = query_template.format(correct_answer=correct_answer, user_guess=user_guess)  + scoreResponseFormat
    # Send query to Gemini API and get response
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(refined_query)
        # Check if the response contains candidates and valid content
        if response and response.candidates:
            candidate = response.candidates[0]
            content_text = candidate.content.parts[0].text.strip()

            # Assuming the content text is in a JSON-compatible format, parse it
            try:
                # Parse the response content to JSON
                content_text = content_text.strip("```json").strip("```").strip()
                generated_data = json.loads(content_text)
                score = generated_data.get("scoring", {}).get("score", 0)
                score = int(score)

                return score

            except Exception as e:
                print("Error in response ", e)
                print("Response \n", content_text)
    except Exception as e:
        print(f"Error while getting result: {e}")
        return None

    return None
