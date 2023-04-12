from rest_framework import serializers
from asosiy.models import Bolim,Mahsulot,Izoh
from django.db.models import Avg

class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bolim
        fields="__all__"
class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mahsulot
        fields="__all__"


    def to_representation(self, instance):
        malumot=super().to_representation(instance)
        malumot['yangi_narx']=instance.narx-(instance.narx*instance.narx/100)
            # quyidagi kod umumiy narxni chiqaradi chegirma bilan

        izoh=Izoh.objects.filter(mahsulot_fk=instance)
        avg_izoh=izoh.aggregate(Avg('reyting'))['reyting__avg']
        malumot["o'rtacha_reyting"]=avg_izoh



        return malumot

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