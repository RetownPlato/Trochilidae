from rest_framework import serializers
from ..models import Car_Model, Car_Check, Car_User
class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Model
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']

class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Check
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_User
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']