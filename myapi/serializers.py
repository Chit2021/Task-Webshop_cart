#Import the Cart model
#Import the REST Framework serializer
#Create a new class that links the Cart with its serializer

from .models import Cart
from rest_framework import serializers

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('id','item_id','item_name', 'item_price')
        