from rest_framework import serializers

from .models import Menu, Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)
    class Meta:
        model = Menu
        fields = ['id', 'date', 'day_period', 'meals']
