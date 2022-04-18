from rest_framework import viewsets
from .serializers import SobreviventesSerializers
from ..models import Sobreviventes


class SobreviventesViewsets(viewsets.ModelViewSet):
 serializer_class = SobreviventesSerializers
 queryset = Sobreviventes.objects.all()
 