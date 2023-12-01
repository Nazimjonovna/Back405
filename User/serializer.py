from  rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')



class EditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)
        # readonly_field = ('username', 'password')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"





























