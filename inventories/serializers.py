from rest_framework import serializers
from . import models



class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id_warehouse', 'name', 'location', 'creation_date', 'update_date',)
        model = models.Warehouse
        

class ShelveSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id_shelve', 'name', 'capacity', 'warehouse', 'creation_date', 'update_date',)
        model = models.Shelve

