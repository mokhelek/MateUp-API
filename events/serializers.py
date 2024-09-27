from rest_framework import serializers
from .models import ChessEvent

class ChessEventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')

    class Meta:
        model = ChessEvent
        fields = ['id', 'name', 'description', 'event_type', 'date', 'location', 'organizer', 'status']

    def create(self, validated_data):
        validated_data['organizer'] = self.context['request'].user
        return super().create(validated_data)
