import status
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from .serializer import *
from .models import *
class BolimAPISerializer(APIView):
    def get(self,request):
        bolim=Bolim.objects.all()
        serializer=BolimSerializer(bolim,many=True)
        return Response(serializer.data)
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