from django import forms


class StartGameForm(forms.Form):
    score = forms.IntegerField(widget=forms.HiddenInput(), initial=0)


class AnswerForm(forms.Form):
    answer = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "ans-input",
                "style": "border: none; outline: none; width: 100%;",
                "placeholder": "Type your answer here...",
            }
        ),
    )


class ScoreForm(forms.Form):
    score = forms.IntegerField(widget=forms.HiddenInput())
