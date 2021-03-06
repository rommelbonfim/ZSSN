# Generated by Django 4.0.4 on 2022-04-17 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sobreviventes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome do sobrevivente')),
                ('idade', models.IntegerField(default=1, verbose_name='Idade')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhuma das opções')], max_length=1)),
                ('item1', models.CharField(choices=[('Água', 'Água'), ('Alimentação', 'Alimentação'), ('Medicação', 'Medicação'), ('Munição', 'Munição')], max_length=100)),
                ('item2', models.CharField(choices=[('Água', 'Água'), ('Alimentação', 'Alimentação'), ('Medicação', 'Medicação'), ('Munição', 'Munição')], max_length=100)),
                ('item3', models.CharField(choices=[('Água', 'Água'), ('Alimentação', 'Alimentação'), ('Medicação', 'Medicação'), ('Munição', 'Munição')], max_length=100)),
                ('item4', models.CharField(choices=[('Água', 'Água'), ('Alimentação', 'Alimentação'), ('Medicação', 'Medicação'), ('Munição', 'Munição')], max_length=100)),
                ('latitude', models.IntegerField(default=0, verbose_name='Informe a latitude de sua localização')),
                ('longitude', models.IntegerField(default=0, verbose_name='Informe a longitude de sua localização')),
                ('infectado', models.BooleanField(default=False, verbose_name='infectado?')),
            ],
        ),
    ]
