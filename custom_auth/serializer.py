from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Test


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ResgisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"
