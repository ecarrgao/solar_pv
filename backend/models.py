from django.db import models
from solarpv.models import *

class Location(models.Model):
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    postal_code = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    fax_number = models.CharField(max_length=15)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.client)

class TestStandard(models.Model):
    standard_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    published_date = models.DateField()

    def __str__(self):
        return str(self.standard_name)

class Product(models.Model):
    model_number = models.CharField(max_length=7)
    product_name = models.CharField(max_length=50)
    cell_technology = models.CharField(max_length=50)
    cell_manufacturer = models.CharField(max_length=50)
    number_of_cells = models.IntegerField()
    number_of_cells_in_series = models.IntegerField()
    number_of_series_strings = models.IntegerField()
    number_of_diodes = models.IntegerField()
    product_length = models.FloatField()
    product_width = models.FloatField()
    product_weight = models.FloatField()
    superstrate_type = models.CharField(max_length=50)
    superstrate_manufacturer = models.CharField(max_length=50)
    substrate_type = models.CharField(max_length=50)
    substrate_manufacturer = models.CharField(max_length=50)
    frame_type = models.CharField(max_length=50)
    frame_adhesive = models.CharField(max_length=50)
    encapsulant_type = models.CharField(max_length=50)
    encapsulant_manufacturer = models.CharField(max_length=50)
    junction_box_type = models.CharField(max_length=50)
    junction_box_manufacturer = models.CharField(max_length=50)

    def __str__ (self):
        return str(self.model_number)

class TestSequence(models.Model):
    sequence_name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.sequence_name)

class PerformanceData(models.Model):
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequence = models.ForeignKey(TestSequence, on_delete=models.CASCADE)
    max_system_voltage = models.FloatField()
    voc = models.FloatField()
    isc = models.FloatField()
    vmp = models.FloatField()
    imp = models.FloatField()
    pmp = models.FloatField()
    ff = models.FloatField()

    def __str__(self):
        return str(self.model_number)

class Service(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    is_fl_required = models.BooleanField()
    fl_frequency = models.FloatField()
    standard = models.ForeignKey(TestStandard, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.service_name)

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_number = models.IntegerField()
    issue_date = models.DateField()
    standard = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
