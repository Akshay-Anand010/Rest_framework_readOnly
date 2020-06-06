from rest_framework import serializers
from .models import Description


class DescriptionSerializer(serializers.ModelSerializer):
    #serializes the description

    class Meta:
        model=Description
        fields=['id','weather_description','temprature','created_on']
