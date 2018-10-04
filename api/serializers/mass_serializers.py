from rest_framework import serializers

from api.models.mass_models import Song, MassMoment, Mass, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class MassMomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MassMoment
        fields = ['moment_name', 'reflection', 'songs']


class MassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mass
        fields = '__all__'
        depth = 2


class RetrieveMassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mass
        fields = ['id', 'day', 'description', 'mass_moments']
        depth = 2
