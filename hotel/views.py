from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from hotel.models import *
from hotel.serializers import *

# Create your views here.
class HotelOp(ReadOnlyModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSer

class AddressOp(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSer

class MenuOp(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = Menuser

class WaiterOp(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = Waiterser
