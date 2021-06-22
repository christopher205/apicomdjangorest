from rest_framework import serializers
from apis.models import Celulares


class CelularesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celulares
        fields = ['id',
                  'modelo',
                  'fabricante',
                  'ano']
