#
# from django.contrib import admin
from django.urls import path,include
from .views import *
#
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('mahsulot',MahsulotAPISerializer)
#
urlpatterns = [
    path('',BolimAPISerializer.as_view()),
    path('bolim/<int:son>',BolimDetailView.as_view()),
    path('izoh/',IzohAPISerializer.as_view()),
    path('', include(router.urls)),
    path('bitamahsulot/<int:son>',TanlanganAPIView.as_view()),
    path('mahsulot/<int:pk>/izohlar',IzohlarApiView.as_view()),
    path('izoh_ochir/<int:pk>/',IzohOchirApiView.as_view()),


]