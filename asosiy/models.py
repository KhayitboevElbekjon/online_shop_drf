from django.db import models
from userapp.models import Profil


class Bolim(models.Model):
    nom=models.CharField(max_length=25)
    rasm=models.FileField(null=True,blank=True)
class Mahsulot(models.Model):
    nom=models.CharField(max_length=25)
    narx=models.IntegerField()
    chegirma=models.IntegerField()
    brend=models.CharField(max_length=25)
    batafsil=models.TextField()
    rasm=models.FileField(null=True,blank=True)
    bolim_fk=models.ForeignKey(Bolim,on_delete=models.CASCADE,null=True)
    holat=models.CharField(max_length=25)
    mavjud=models.BooleanField()
    sotuvchi_fk=models.ForeignKey(Profil,on_delete=models.CASCADE,null=True)
class Izoh(models.Model):
    profil_fk=models.ForeignKey(Profil,on_delete=models.CASCADE)
    matn=models.TextField()
    reyting=models.SmallIntegerField(max_length=25)
    mahsulot_fk=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    sana=models.DateTimeField()
