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
        depth = 1


class MassMomentSerializer(serializers.ModelSerializer):
    songs = SongSerializer(read_only=True, many=True)

    class Meta:
        model = MassMoment
        fields = ['moment_name', 'reflection', 'songs']


class MassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mass
        fields = '__all__'


class RetrieveMassSerializer(serializers.ModelSerializer):
    mass_moments = MassMomentSerializer(read_only=True, many=True)

    class Meta:
        model = Mass
        fields = ['id', 'day', 'description', 'mass_moments']
