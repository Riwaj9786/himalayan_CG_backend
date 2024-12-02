from django.urls import path
from UserProfile.views import (
    BoardOfDirectorsListAPIView,
    TeamListAPIView,
    ProfileDetailView
)


urlpatterns = [
    path('BoDs/', BoardOfDirectorsListAPIView.as_view(), name='board_of_directorrs'),
    path('teams/', TeamListAPIView.as_view(), name='team_list'),
    path('profile/<str:uuid>/', ProfileDetailView.as_view(), name='profile-detail'),
]