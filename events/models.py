from django.db import models
from django.contrib.auth.models import User



class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class ChessEvent(models.Model):
    EVENT_TYPES = (
        ('rated', 'rated'),
        ('casual', 'casual'),
        ('online', 'online'),
        ('study', 'study'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    )
    
    event_poster = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=255) 
    description = models.TextField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES) 
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255) 
    tags = models.ManyToManyField(Tag, related_name='posts', default='chessa') #*
    created_at = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending') 
    
    def __str__(self):
        return self.name
