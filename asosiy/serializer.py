from rest_framework import serializers
from asosiy.models import Bolim,Mahsulot,Izoh


class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bolim
        fields="__all__"
class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mahsulot
        fields="__all__"
    def validate_chegirma(self,qiymat):
        if qiymat<-1 and qiymat>51:
            raise serializers.ValidationError("Chegirma 0 dan kichik yoki 50 dan baland foizda bo'lishi mumkin emas")
        return qiymat
class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model=Izoh
        fields="__all__"
    def validate_reyting(self,qiymat):
        if qiymat>6 and qiymat<0:
            raise serializers.ValidationError("Siz kiritayotgan reyting 1~5 oraliqdan chiqib keti!")
        return qiymat