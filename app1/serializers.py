from rest_framework import serializers
from .models import *

class DataConverter(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'
        # fields = ('first_name', 'email', 'password')