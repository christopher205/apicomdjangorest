from rest_framework import viewsets
from apis.models import Celulares
from apis.serializer import CelularesSerializer


class CelularViewSet(viewsets.ModelViewSet):

    queryset = Celulares.objects.all()
    serializer_class = CelularesSerializer