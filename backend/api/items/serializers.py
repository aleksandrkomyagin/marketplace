from rest_framework import serializers
from items.models import Items


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = (
            "id", "name", "description", "price"
        )
