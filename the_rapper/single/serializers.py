from rest_framework import serializers
from .models import Single

class SingleSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()
    class Meta:
        model =  Single
        fields = ['name', 'youtube_views', 'artist']

    def get_artist(self, instance):
        return instance.artist.name