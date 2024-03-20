from django.db import models


class CallHistory(models.Model):
    endpoint = models.CharField(max_length=100)
    result = models.TextField()
    call_date = models.DateTimeField()

