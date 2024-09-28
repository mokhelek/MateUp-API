from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('events/', views.chess_event_list, name='chess_event_list'),
    path('events/<int:pk>/', views.chess_event_detail, name='chess_event_detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tags/', views.get_tags, name='get_tags'),
]
