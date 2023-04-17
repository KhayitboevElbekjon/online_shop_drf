from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from userapp.models import Profil


class BuyurtmaApiView(APIView):
    def get(self,request):
        buyurtma=Buyurtma.objects.filter(profil_fk__user_fk=request.user)
        serializer=BuyurtmaSerializer(buyurtma,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=BuyurtmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profil_fk=Profil.objects.get(user_fk=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SavatItemApiView(APIView):
    def get(self,request):
        savat=Savat.objects.get(profil_fk__user_fk=request.user)
        savat_item=Savatitem.objects.get(savat_fl=savat)
        serializerr=SavatItemApiView(savat_item,many=True)
        return Response(serializerr.data)