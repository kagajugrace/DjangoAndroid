from rest_framework import serializers
from .models import *

from django.http import JsonResponse

# class PostSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=Posts
#         fields =('_all_')

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model= Pharmacy
        depth=1
        fields=('__all__')

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model= Medicine
        depth=1
        fields=('__all__')

class KipharmaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Kipharma
        depth=1
        fields=('__all__')

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Postnews
        fields =('_all_')