from django.contrib.auth.models import User
from django.db import models
class Profil(models.Model):
    ism=models.CharField(max_length=25)
    rasm=models.FileField(blank=True,null=True)
    tel=models.CharField(max_length=13)
    user_fk=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    tugulgan_yil=models.DateField()
    jins=models.CharField(max_length=6)
    shaxar=models.CharField(max_length=50)



