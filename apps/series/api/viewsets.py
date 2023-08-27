from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.series.api.serializers import *
from apps.series.models import *

class serieViewset(viewsets.ModelViewSet):
 
    
    serializer_class = SerieSerializer

    def get_queryset(self, pk=None):

        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    def create(self, request, *args, **kwargs):

        serializer = SerieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                    {"message": "Serie agregada con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )

    def list(self, request):
        series_serializer = self.serializer_class(self.get_queryset(), many=True)
        data =  series_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        serie = self.get_queryset(pk)
        if serie:
            serie_serializer = self.serializer_class(serie)
            return Response(serie_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe una serie con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Serie actualizada con exito!"}, status=status.HTTP_200_OK)

class temporadaViewset(viewsets.ModelViewSet):
 
    
    serializer_class = temporadaSerializer

    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    def create(self, request, *args, **kwargs):
        serializer = temporadaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                    {"message": "temporada agregada con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )

    def list(self, request):
        
        temporadas_serializer = self.serializer_class(self.get_queryset(), many=True)
        data =  temporadas_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        temporada = self.get_queryset(pk)
        if temporada:
            temporada_serializer = self.serializer_class(temporada)
            return Response(temporada_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe una temporada con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def partial_update(self, request, pk=None):

        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "temporada actualizada con exito!"}, status=status.HTTP_200_OK)
