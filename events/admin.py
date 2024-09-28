from django.contrib import admin
from .models import ChessEvent, Tag

# Register your models here.

admin.site.register(ChessEvent)
admin.site.register(Tag)