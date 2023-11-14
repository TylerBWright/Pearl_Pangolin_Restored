from django.forms import ModelForm
from pp.models import Submission


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = [
            "question",
            "answer",
        ]
