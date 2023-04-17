from django.db import models
from django.db.models import Sum

from userapp.models import *
from asosiy.models import *




class Tanlanganlar(models.Model):
    profil_fk=models.ForeignKey(Profil,on_delete=models.CASCADE)
    mahsulot_fk=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)

class Savat(models.Model):
    profil_fk=models.ForeignKey(Profil,on_delete=models.CASCADE)
    ochilgan_sana = models.DateField(auto_now_add=True,null=True)
class Savatitem(models.Model): # savatdan olingan mahsulotlarni saqlash uchun
    mahsulot_fk = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor=models.PositiveSmallIntegerField(default=1)
    yetkazish_kuni=models.PositiveSmallIntegerField(default=4)
    savat_fl=models.ForeignKey(Savat,on_delete=models.CASCADE,related_name='itemlari')
    umumiy_summa=models.IntegerField(blank=True,null=True)
    yetkazish_puli=models.PositiveSmallIntegerField(default=15000)
    def save(self, *args,**kwargs):
        self.umumiy_summa=(self.miqdor*(self.mahsulot_fk.narx-(self.mahsulot_fk.narx*self.mahsulot_fk.chegirma/100)))+self.yetkazish_puli
        super().save(*args,**kwargs)
class Buyurtma(models.Model):
    profil_fk=models.ForeignKey(Profil,on_delete=models.CASCADE)
    savat_fk = models.ForeignKey(Savat, on_delete=models.CASCADE)
    holat=models.CharField(max_length=50)
    sana=models.DateField(auto_now_add=True)
    umumiy_summa=models.IntegerField(null=True,blank=True)
    def save(self, *args,**kwargs):
        itemlar=self.savat_fk.itemlari.all()
        self.umumiy_summa=itemlar.aggregate(summasi=Sum('umumiy_summa')).get('summasi')      # summasi:45164654
        super().save(*args,**kwargs)





