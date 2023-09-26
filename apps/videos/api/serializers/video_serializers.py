from rest_framework import serializers
from apps.videos.models import Categoria, Idioma, Video
from apps.series.api.serializers import *
from apps.videos.api.serializers.general_serializers import (
    CategoriaSerializerV,
    IdiomaSerializer,
    IdiomaSerializerV,
    tipoVideoSerializer,
    CategoriaSerializer,
    EspecialidadSerializer,
    EspecialidadSerializerV,
    SubEspecialidadSerializer,
    SubEspecialidadSerializerV
)

#serializer for create and update
class VideoSerializer(serializers.ModelSerializer):
    tipe_of_video = tipoVideoSerializer
    temporada = temporadaSerializer
    languages = IdiomaSerializerV(many=True, queryset=Idioma.objects.all())
    categorias = CategoriaSerializerV(many=True, queryset=Categoria.objects.all())
    especialidad = EspecialidadSerializerV(many=True, queryset=Categoria.objects.all())
    subEspecialidad = SubEspecialidadSerializerV(many=True, queryset=Categoria.objects.all())
    class Meta:
        model = Video
        fields = [
            "id",
            "code_esp",
            "code_engl",
            "title_espanol",
            "title_english",
            "title_cap_esp",
            "title_cap_english",
            "description_esp",
            "description_english",
            "duration",
            "featured_image",
            "min_image",
            "score",
            "cumulative_score",
            "numberOfVotes",
            "tipe_of_video",
            "state",
            "upload_date",
            "create_date",
            "categorias",
            "languages",
            "especialidad",
            "subEspecialidad"
        ]

    def create(self, validated_data):
        categorias = validated_data.pop("categorias")
        especialidad = validated_data.pop("especialidad")
        subEspecialidad = validated_data.pop("subEspecialidad")
        idioms = validated_data.pop("languages")

        instance = Video.objects.create(
            **validated_data
        )  # se crea el objeto del formulario json para Video
        for i in idioms:
            instance.languages.add(i.id)  # se guarda la relacion m2m

        for j in categorias:
            instance.categorias.add(j.id) # se guarda la relacion m2m

        for j in especialidad:
            instance.especialidad.add(j.id) # se guarda la relacion m2m

        for j in subEspecialidad:
            instance.subEspecialidad.add(j.id) # se guarda la relacion m2m

        return instance

#serializer for list and retrieve
class VideoSerializer2(serializers.ModelSerializer):
    tipe_of_video = tipoVideoSerializer
    temporada = temporadaSerializer
    languages = IdiomaSerializer(many=True)
    categorias = CategoriaSerializer(many=True)
    especialidad = EspecialidadSerializer(many=True)
    subEspecialidad = SubEspecialidadSerializer(many=True)


    class Meta:
        model = Video
        fields = [
            "id",
            "code_esp",
            "code_engl",
            "title_espanol",
            "title_english",
            "title_cap_esp",
            "title_cap_english",
            "description_esp",
            "description_english",
            "duration",
            "featured_image",
            "min_image",
            "score",
            "cumulative_score",
            "numberOfVotes",
            "tipe_of_video",
            "state",
            "upload_date",
            "create_date",
            "categorias",
            "languages",
            "especialidad",
            "subEspecialidad",
            "temporada",
        ]
