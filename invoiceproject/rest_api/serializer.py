from rest_framework import serializers
from .models import Registration,Login


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields=("firstName","lastName","email","phone")

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields="__all__"        
