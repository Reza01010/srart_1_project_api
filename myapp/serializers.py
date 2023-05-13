
from rest_framework import serializers

from .models import Item, JonyurUser, Jonyur  # import model


class ItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Item
        fields = '__all__'


class JonyurUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = JonyurUser
        fields = ['age', 'last_name', 'first_name']

    def validate(self, data):
        if 'age' in data and data['age'] < 18:
            data['age'] = "Under 18 years old"

        return data


class JonyurSerializer(serializers.ModelSerializer):
    user = JonyurUserSerializer(read_only=True)

    class Meta:
        model = Jonyur
        fields = ['id', 'text', 'user']


