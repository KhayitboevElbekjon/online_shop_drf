# Generated by Django 3.2.18 on 2023-04-17 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
        ('buyurtma', '0003_auto_20230417_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holat', models.CharField(max_length=50)),
                ('sana', models.DateField(auto_now_add=True)),
                ('umumiy_summa', models.IntegerField()),
                ('profil_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
                ('savat_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyurtma.savat')),
            ],
        ),
    ]
