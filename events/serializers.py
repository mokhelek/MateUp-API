from rest_framework import serializers
from .models import ChessEvent, Tag

class ChessEventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    
    class Meta:
        model = ChessEvent
        fields = ['id', 'name', 'description', 'event_type', 'start_date','end_date',  'location', 'organizer', 'status', 'tags']

    def create(self, validated_data):
        validated_data['organizer'] = self.context['request'].user
        return super().create(validated_data)
    
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        
        