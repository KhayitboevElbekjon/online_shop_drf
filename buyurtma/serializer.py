from .models import *
from rest_framework import serializers
class SavatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Savat
        fields="__all__"
class SavatItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Savatitem
        fields="__all__"


class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Buyurtma
        fields='__all__'
