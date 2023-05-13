from django.db import models
from django.core import validators


class Item(models.Model):
    name = models.CharField(max_length=50)

    title = models.CharField(max_length=210)

    body = models.TextField()

    def __str__(self):
        return self.title


class JonyurUser(models.Model):
    age = models.PositiveIntegerField(
        validators=[validators.MaxValueValidator(120)]
    )
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)


class Jonyur(models.Model):
    user = models.ForeignKey(JonyurUser, on_delete=models.CASCADE, related_name='user')
    text = models.CharField(max_length=300)
