from django.urls import path
from UserProfile.views import ProfileAPIView, BoardofDirectorsUpdateAPIView, BoardOfDirectorsListCreateAPIView, TeamRetrieveUpdateDestroyAPIView, UpdateProfileAPIView, TeamAPIView

urlpatterns = [
    path('profile/', ProfileAPIView.as_view(), name='profile_list'),
    path('profile/<pk>/', ProfileAPIView.as_view(), name='profile_detail'),
    path('profile/<pk>/update_image/', UpdateProfileAPIView.as_view(), name='profile_picture'),
    path('team/', TeamAPIView.as_view(), name='team-list'),
    path('team/<pk>/', TeamRetrieveUpdateDestroyAPIView.as_view(), name='team-detail-update'),
    path('BoDs/', BoardOfDirectorsListCreateAPIView.as_view(), name='board_of_directors'),
    path('BoDs/<pk>/', BoardofDirectorsUpdateAPIView.as_view(), name='BoD-detail-update'),
]