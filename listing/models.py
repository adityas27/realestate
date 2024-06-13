from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here


class Location(models.Model):
    address_1 = models.CharField(max_length=255, help_text="Flat No. and building no./House no. etc..", default="")
    address_2 = models.CharField(max_length=255, help_text="Building name/society name/etc....", default="")
    address_3 = models.CharField(max_length=255, help_text="Road name/Locality and landmark.. etc...", default="")
    address_4 = models.CharField(max_length=255, help_text="Town name/city name-district name-state name", default="")
    pincode = models.IntegerField(default=0, help_text="Pincode for eg: 400001 for mumbai")
    city = models.CharField(max_length=255, help_text="CITY")
    state = models.CharField(max_length=255, help_text="STATE")
    nation = models.CharField(max_length=255, help_text="NATION")

class ImportantFigures(models.Model):
    area = models.IntegerField()
    lot_area = models.IntegerField(null=True, blank=True)
    no_of_floors = models.IntegerField(null=True)
    ground_to_floor = models.IntegerField(help_text="in ft")
    beds = models.IntegerField()
    baths = models.IntegerField()
    garage = models.IntegerField()

class Property(models.Model):
    PROP_TYPE_CHOICES = [
        ('flat', 'Apartment/Flat'),
        ('house', 'Single Family House'),
        ('condonium', 'Condonium'),
        ('bungalow', 'Bungalow'),
    ]
    OWN_TYPE_CHOICE = [
        ('rent', 'Rent'),
        ('buy', 'Buy'),
    ]
    id = models.UUIDField( 
             primary_key = True, 
             default = uuid.uuid4, 
             editable = False)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    dimensions = models.OneToOneField(ImportantFigures, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    year_built = models.IntegerField()
    furnished = models.BooleanField(help_text="Wether or not property is furnished", default=False)
    prop_type = models.CharField(max_length=10, choices=PROP_TYPE_CHOICES)
    own_type = models.CharField(max_length=10, choices=OWN_TYPE_CHOICE, default="buy")
    desc = models.TextField(default="")
    visits = models.IntegerField(help_text="number of visits this week", default=0)
    hidden = models.BooleanField(help_text="If you want to hide a specific listing", default=False)
    thumbnail = models.ImageField(help_text="Thumbnail image", null=True, upload_to='property_images')
    def __str__(self):
        return f"{self.location.address_2}:{self.location.address_1}-{self.year_built}"

class Picture(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    for_list = models.ForeignKey(Property, on_delete=models.CASCADE, primary_key=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, primary_key=False)
    image = models.ImageField(upload_to=f'property_image')
    date_time = models.DateTimeField(auto_now=True, editable=False)
