from rest_framework import serializers
from .models import Registration


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields=("First_Name","Last_Name","Email","Phone")
