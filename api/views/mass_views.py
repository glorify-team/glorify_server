from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from api.models.mass_models import Author, Song, Mass, MassMoment
from api.serializers.mass_serializers import \
    SongSerializer, AuthorSerializer, MassSerializer, MassMomentSerializer, RetrieveMassSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class MassViewSet(viewsets.ViewSet):
    queryset = Mass.objects.all()

    def list(self, _request):
        queryset = Mass.objects.all()
        serializer = MassSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, _request, pk=None):
        mass = get_object_or_404(self.queryset, pk=pk)
        serializer = RetrieveMassSerializer(mass)
        return Response(serializer.data)


class MassMomentViewSet(viewsets.ModelViewSet):
    queryset = MassMoment.objects.all()
    serializer_class = MassMomentSerializer
