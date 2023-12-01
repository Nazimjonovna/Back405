from rest_framework import serializers
from .models import Multik

class HomeSRL(serializers.ModelSerializer):
    class Meta:
        model = Multik
        fields = '__all__'



