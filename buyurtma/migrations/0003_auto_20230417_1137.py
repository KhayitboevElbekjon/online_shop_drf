# Generated by Django 3.2.18 on 2023-04-17 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma', '0002_auto_20230417_1117'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Buyurtma',
        ),
        migrations.AddField(
            model_name='savatitem',
            name='yetkazish_puli',
            field=models.PositiveSmallIntegerField(default=15000),
        ),
        migrations.AlterField(
            model_name='savatitem',
            name='savat_fl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemlari', to='buyurtma.savat'),
        ),
    ]
