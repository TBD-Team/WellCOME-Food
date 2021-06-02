from rest_framework import serializers

from .models import Account, Credit, GRU, Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit

