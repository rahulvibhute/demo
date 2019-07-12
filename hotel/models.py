from django.db import models

# Create your models here.

class Hotel(models.Model):
    Hotelname = models.CharField(max_length=50)

    class Meta:
        db_table = "Hotel_Data"

class Address(models.Model):
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    hoteladdresses = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Address_data"

class Menu(models.Model):
    menuname = models.CharField(max_length=50)
    menucode = models.IntegerField()
    price = models.IntegerField()
    hotelmenus = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Menu_data"

class Waiter(models.Model):
    waitername = models.CharField(max_length=50)
    waitercode = models.IntegerField()
    Hotelwaiters = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Waiter_data"
