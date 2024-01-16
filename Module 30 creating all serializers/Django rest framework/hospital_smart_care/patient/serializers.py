from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False) # akhon user = id na dekhay name dekhabe rest framework er interface a

    class Meta:
        model = Patient
        fields = '__all__'