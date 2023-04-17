from django.urls import path,include
from .views import *
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register('mahsulot',MahsulotAPISerializer)
# #
urlpatterns = [
    path('buyurtma/',BuyurtmaApiView.as_view()),
    path('savatitem/',SavatItemApiView.as_view()),


]