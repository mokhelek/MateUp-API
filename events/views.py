from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ChessEvent
from .serializers import ChessEventSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from .models import Tag
from .serializers import TagSerializer


@api_view(['GET', 'POST'])
def chess_event_list(request):
    if request.method == 'GET':
        if request.user.is_staff:
            events = ChessEvent.objects.all().order_by('-created_at')
        else:
            events = ChessEvent.objects.filter(status='approved').order_by('-created_at')
        serializer = ChessEventSerializer(events, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = ChessEventSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Authentication required'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'PUT', 'DELETE'])
def chess_event_detail(request, pk):
    event = get_object_or_404(ChessEvent, pk=pk)

    if request.method == 'GET':
        serializer = ChessEventSerializer(event)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if request.user == event.organizer or request.user.is_staff:
            serializer = ChessEventSerializer(event, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Not authorized to edit this event'}, status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'DELETE':
        if request.user == event.organizer or request.user.is_staff:
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'Not authorized to delete this event'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def get_tags(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)