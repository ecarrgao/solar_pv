from django.db import models
from solarpv.models import *

class Location(models.Model):
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    postal_code = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    fax_number = models.CharField(max_length=15)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.address1

class TestStandard(models.Model):
    standard_name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    published_date = models.DateField()

    def __str__(self):
        return self.standard_name

class Product(models.Model):
    model_number = models.CharField(primary_key=True, max_length=7)
    product_name = models.CharField(max_length=20)
    cell_technology = models.CharField(max_length=20)
    cell_manufacturer = models.CharField(max_length=20)
    number_of_cells = models.IntegerField()
    number_of_cells_in_series = models.IntegerField()
    number_of_series_strings = models.IntegerField()
    number_of_diodes = models.IntegerField()
    product_length = models.FloatField()
    product_width = models.FloatField()
    product_weight = models.FloatField()
    superstrate_type = models.CharField(max_length=20)
    superstrate_manufacturer = models.CharField(max_length=20)
    substrate_type = models.CharField(max_length=20)
    substrate_manufacturer = models.CharField(max_length=20)
    frame_type = models.CharField(max_length=20)
    frame_adhesive = models.CharField(max_length=20)
    encapsulant_type = models.CharField(max_length=20)
    encapsulant_manufacturer = models.CharField(max_length=20)
    junction_box_type = models.CharField(max_length=20)
    junction_box_manufacturer = models.CharField(max_length=20)

    def __str__(self):
        return self.product_name

class TestSequence(models.Model):
    sequence_name = models.CharField(max_length=20)

    def __str__(self):
        return self.sequence_name

class PerformanceData(models.Model):
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequence_id = models.ForeignKey(TestSequence, on_delete=models.CASCADE)
    max_system_voltage = models.FloatField()
    voc = models.FloatField()
    isc = models.FloatField()
    vmp = models.FloatField()
    imp = models.FloatField()
    pmp = models.FloatField()
    ff = models.FloatField()

    def __str__(self):
        return self.model_number

class Service(models.Model):
    service_name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    is_fl_required = models.BooleanField()
    fl_frequency = models.FloatField()
    standard_id = models.ForeignKey(TestStandard, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name

class Certificate(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    report_number = models.IntegerField()
    issue_date = models.DateField()
    standard_id = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.report_number
