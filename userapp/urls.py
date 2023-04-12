from django.urls import path,include
from .views import *

urlpatterns = [
    path('usercreate/',UserCreateAPI.as_view()),
    path('profilcreate/',ProfilCreateAPI.as_view()),

]