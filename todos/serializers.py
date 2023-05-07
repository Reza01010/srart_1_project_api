
from rest_framework import serializers

from .models import Todo  # import model


# Create a class


class TodoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Todo
        fields = ('id', 'title', 'body', )


