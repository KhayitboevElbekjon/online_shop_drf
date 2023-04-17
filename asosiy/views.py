import status
from django.contrib.auth import *
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from .serializer import *
from .models import *
class BolimAPISerializer(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            bolim=Bolim.objects.all()
            serializer=BolimSerializer(bolim,many=True)
            return Response(serializer.data)
        return Response({'xabar':'login qilinmagan'})
class BolimDetailView(APIView):
    def get(self,request,son):
        bolim=Bolim.objects.get(id=son)
        serializer=BolimSerializer(bolim)
        return Response(serializer.data)
class IzohAPISerializer(APIView):
    def get(self,request):
        izoh=Izoh.objects.all()
        serializer=IzohSerializer(izoh,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=IzohSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MahsulotAPISerializer(ModelViewSet):
    # def get(self,request):
    #     mahsulot=Mahsulot.objects.all()
    #     serializer=MahsulotSerializer(mahsulot,many=True)
    #     return Response(serializer.data)
    # def post(self,request):
    #     serializer=MahsulotSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
    def get_queryset(self):
        nomm=self.request.query_params.get('qidirish')
        if nomm is None or nomm=='':
            natija=Mahsulot.objects.all()
        else:
            natija=Mahsulot.objects.filter(nom__contains=nomm)
        return natija
class TanlanganAPIView(APIView):
    def get(self,request,son):
        mahsulot=Mahsulot.objects.get(id=son)
        serializer=MahsulotSerializer(mahsulot)
        return Response(serializer.data)

class IzohlarApiView(APIView):
    def get(self,request,pk):
        izohlar=Izoh.objects.filter(mahsulot_fk__id=pk)
        serializer=IzohSerializer(izohlar,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,pk):
        serializer=IzohSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                profil_fk=Profil.objects.get(user_fk=request.user),
                mahsulot_fk=Mahsulot.objects.get(id=pk)
            )
            natija=serializer.data
            natija['mahsulot_fk']=pk
            natija['profil_fk']=Profil.objects.get(user_fk=request.user).id
            return Response(natija)
        return Response(serializer.errors)
class IzohOchirApiView(APIView):
    def delete(self,request,pk):
        Izoh.objects.get(id=pk).delete()
        return Response({'xabar':"Izoh o'chirilldi"},status=status.HTTP_200_OK)
