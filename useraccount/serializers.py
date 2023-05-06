from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        # exclude = ['password']
        fields = "__all__"
        depth = 1