from rest_framework import serializers

from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreditCard
        fields = '__all__'
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'
class TypeServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TypeService
        fields = '__all__'