from django.urls import path,include
from .views import *

urlpatterns = [
    path('usercreate/',UserCreateAPI.as_view()),
    path('profilcreate/',ProfilCreateAPI.as_view()),
    path('tanlanganprofil/<int:pk>',TanlanganProfilView.as_view()),
    path('login/',LoginApiView.as_view()),
    path('logout/',LogautView.as_view()),

]