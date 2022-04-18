from django.db import models

class Sobreviventes(models.Model):

 SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

 ITEM_CHOICES = (
        ("Água", "Água"),
        ("Alimentação", "Alimentação"),
        ("Medicação", "Medicação"),
        ("Munição", "Munição")
    )

 nome = models.CharField('Nome do sobrevivente', max_length=250)
 idade = models.IntegerField('Idade', default=1)
 sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
 item1 = models.CharField(max_length=100, choices=ITEM_CHOICES, blank=False, null=False)
 item2 = models.CharField(max_length=100, choices=ITEM_CHOICES, blank=False, null=False)
 item3 = models.CharField(max_length=100, choices=ITEM_CHOICES, blank=False, null=False)
 item4 = models.CharField(max_length=100, choices=ITEM_CHOICES, blank=False, null=False)
 latitude = models.IntegerField('Informe a latitude de sua localização', default=0)
 longitude = models.IntegerField('Informe a longitude de sua localização', default=0)
 infectado = models.BooleanField('infectado?', default=False)
 
 def __str__(self):
  return str(self.nome)

