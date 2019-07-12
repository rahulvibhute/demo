from rest_framework.serializers import ModelSerializer
from hotel.models import *


class HotelSer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class AddressSer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class Menuser(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class Waiterser(ModelSerializer):
    class Meta:
        model = Waiter
        fields = '__all__'