from rest_framework import serializers
from ..models import Sobreviventes

class SobreviventesSerializers(serializers.ModelSerializer):
 class Meta:
  model = Sobreviventes
  fields = "__all__"
