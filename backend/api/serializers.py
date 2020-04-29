from rest_framework import serializers
from ..models import Product, Service, Certificate

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    standard = serializers.StringRelatedField()
    location = serializers.StringRelatedField()
    class Meta:
        model = Certificate
        fields = '__all__'
