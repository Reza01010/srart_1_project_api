from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)

    title = models.CharField(max_length=210)

    body = models.TextField()

    def __str__(self):
        return self.title
