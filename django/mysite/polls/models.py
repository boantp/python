from django.db import models

# Create your models here.
class VehicleCountry(models.Model):
    vehicle_country_name = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.vehicle_country_name

    class Meta:
        db_table = 'vehicle_country'

class VehicleBrand(models.Model):
    vehicle_country = models.OneToOneField(VehicleCountry)
    vehicle_brand_id = models.IntegerField(null=True, blank=True)
    vehicle_brand_name = models.CharField(max_length=100, blank=True)
    vehicle_brand_description = models.CharField(max_length=100, blank=True)
    #vehicle_brand_country_id = models.ForeignKey(VehicleCountry, db_column='vehicle_country_id')

    def __unicode__(self):
        return self.vehicle_brand_name

    class Meta:
        db_table = 'vehicle_brand'

class VehicleModel(models.Model):
    vehicle_model_id = models.IntegerField(null=True, blank=True)
    vehicle_brand_id = models.ForeignKey(VehicleBrand, db_column='vehicle_brand_id')
    vehicle_country_id = models.ForeignKey(VehicleCountry, db_column='vehicle_country_id')
    vehicle_model_name = models.CharField(max_length=100, default='', blank=True)

    def __unicode__(self):
        return self.vehicle_model_name

    class Meta:
        db_table = 'vehicle_model'

class VehicleType(models.Model):
    vehicle_type_id = models.IntegerField(null=True, default='', blank=True)
    vehicle_type_name = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.vehicle_type_name

    class Meta:
        db_table = 'vehicle_type'

class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100, blank=True)
    vehicle_brand_id = models.ForeignKey(VehicleBrand, db_column='vehicle_brand_id')
    vehicle_country_id = models.ForeignKey(VehicleCountry, db_column='vehicle_country_id')
    vehicle_model_id = models.ForeignKey(VehicleModel, db_column='vehicle_model_id')
    vehicle_type_id = models.ForeignKey(VehicleType, default='', db_column='vehicle_type_id')

    def __unicode__(self):
        return self.vehicle_name

    class Meta:
        db_table = 'vehicle'


