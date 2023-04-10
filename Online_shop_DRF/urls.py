
from django.contrib import admin
from django.urls import path,include
from asosiy.views import *

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('bolim',BolimAPISerializer)

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
