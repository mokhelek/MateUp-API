from django.db import models
from django.contrib.auth.models import User

class ChessEvent(models.Model):
    EVENT_TYPES = (
        ('rated', 'Rated Tournament'),
        ('casual', 'Casual Tournament'),
        ('social', 'Social Chess Meetup'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    def __str__(self):
        return self.name
