from django.conf import settings
from django.conf.urls.static import static


# from django.contrib import admin
# from django.urls import path,include
# from asosiy.views import *
#
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register('bolim',BolimAPISerializer)

from django.contrib import admin
from django.urls import path,include

from asosiy.views import BolimAPISerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Asosiy/',include('asosiy.urls')),
    path('Userapp/',include('userapp.urls')),
    path('buyurtma/',include('buyurtma.urls')),
    # path('',include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
