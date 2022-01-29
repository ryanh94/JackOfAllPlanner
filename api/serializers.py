from dataclasses import fields
import imp
from rest_framework import serializers
from base.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("firstname", "lastname")