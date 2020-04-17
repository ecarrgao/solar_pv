from rest_framework import serializers
from ..models import Product, Certificate, Service

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
