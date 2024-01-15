from rest_framework import serializers
from .models import *

class MealSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class MealSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=300)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Meal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
