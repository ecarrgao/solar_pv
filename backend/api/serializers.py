from rest_framework import serializers
from ..models import Product, Service, Certificate

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['model_number', 'product_name', 'cell_technology',
        'cell_manufacturer', 'number_of_cells', 'number_of_cells_in_series',
        'number_of_series_strings', 'number_of_diodes', 'product_length',
        'product_width', 'product_weight', 'superstrate_type',
        'superstrate_manufacturer', 'substrate_type', 'substrate_manufacturer',
        'frame_type', 'frame_adhesive', 'encapsulant_type',
        'encapsulant_manufacturer', 'junction_box_type',
        'junction_box_manufacturer']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_name', 'description', 'is_fl_required',
        'fl_frequency', 'standard']

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['certificate_number', 'user', 'report_number', 'issue_date', 'standard',
        'location', 'model_number']
