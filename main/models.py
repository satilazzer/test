from django.contrib.auth.models import User
from django.db import models


class Token(models.Model):
    token_code = models.CharField('token_code', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_tg_id = models.CharField(max_length=100, default='')


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateandtime = models.TimeField()
    text = models.TextField()
