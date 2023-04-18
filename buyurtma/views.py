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
        savat_items = Savatitem.objects.filter(savat_fl__profil_fk__user_fk=request.user)
        serializer = SavatItemSerializer(savat_items, many=True)
        return Response(serializer.data)

    def delete(self,request):
        savat=Savat.objects.get(profil_fk__user_fk=request.user)
        savat_item=Savatitem.objects.get(savat_fl=savat).delete()
        return Response({'xabar':"O'chirldi"},status=status.HTTP_200_OK)
    def put(self,request):
        savat_items = Savatitem.objects.filter(savat_fl__profil_fk__user_fk=request.user)
        serializer=SavatItemSerializer(savat_items,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        serializer=SavatItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                savat_fl=Savat.objects.get(profil_fk__user_fk=request.user)
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)