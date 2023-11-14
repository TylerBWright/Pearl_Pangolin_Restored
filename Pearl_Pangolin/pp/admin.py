from django.contrib import admin
from pp.models import Submission


# Register your models here.


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = [
        "question",
        "answer",
    ]
