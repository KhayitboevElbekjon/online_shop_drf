import status
from django.contrib.auth import *
from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework import *
from rest_framework.response import *
from buyurtma.models import *




class UserCreateAPI(APIView):
    def post(self,request):
        serializers=UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class ProfilCreateAPI(APIView):
    def post(self,request):
        serializers=ProfilSerialzier(data=request.data)
        if serializers.is_valid():
            serializers.save()
            Savat.objects.create(profil_fk=Profil.objects.last())
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class TanlanganProfilView(APIView):
    def tanlanganprofil(self,request,pk):
        if request.user.is_authenticated:
            profil=Profil.objects.get(id=pk)
            serializer=ProfilSerialzier(profil)
            return Response(serializer.data)
        return Response({'xabar': 'login qilinmagan'})
    def delete(self,request,pk):
        if request.user.is_authenticated:
            Profil.objects.get(id=pk).delete()
            return Response({'xabar':"Profil o'chirilldi"},status=status.HTTP_200_OK)
        return Response({'xabar': 'login qilinmagan'})
    def put(self,request,pk):
        if request.user.is_authenticated:
            profil = Profil.objects.get(id=pk)
            serializer=ProfilSerialzier(profil,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class LoginApiView(APIView):
    def post(self,request):
        serializer=LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user=authenticate(username=serializer.data['username'],
                         password=serializer.data['password'])
            if user is None:
                return Response({"xabar":"Bunaqa user mavjud emas"},status=status.HTTP_400_BAD_REQUEST)
            login(request, user)
            return Response({"xabar":"Tizimga kiritildi"},status=status.HTTP_200_OK)
        return Response(serializer.errors)
class LogautView(APIView):
    def get(self,request):
        logout(request)
        return Response({"xabar":"User tizimdan muvofiqiyatli chiqaarildi"},status=status.HTTP_200_OK)

