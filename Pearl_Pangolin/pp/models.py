from django.db import models

# Create your models here.


class Submission(models.Model):
    question = models.TextField()
    answer = models.TextField()
