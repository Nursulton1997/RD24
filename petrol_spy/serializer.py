from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import OneIDProfile


class OneIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneIDProfile
        fields = ['first_name', 'last_name']


class UserSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)
    one_id = OneIdSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'count', 'one_id']
