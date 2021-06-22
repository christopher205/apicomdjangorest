from rest_framework import viewsets
from apis.models import Celulares
from apis.serializer import CelularesSerializer
from rest_framework.permissions import IsAuthenticated


class CelularViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Celulares.objects.all()
    serializer_class = CelularesSerializer