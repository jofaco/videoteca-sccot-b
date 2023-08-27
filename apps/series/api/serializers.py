from rest_framework import serializers

from apps.series.models import *

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = "__all__"

class temporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = "__all__"


class temporadaSerializerV(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = "__all__"