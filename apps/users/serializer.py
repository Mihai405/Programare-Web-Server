from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   User
        fields  =   ['email','password','role']
        read_only_fields=['role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance