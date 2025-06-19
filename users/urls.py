from django.urls import path
from .views import FavoriteListCreateView, FavoriteDeleteView
from .views import UserUpdateView
from .views import LoginView
from .views import DashboardView
from .views import RegisterView

urlpatterns = [
    path('update/', UserUpdateView.as_view(), name='user-update'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('favorites/', FavoriteListCreateView.as_view(), name='favorites-list-create'),
    path('favorites/<int:pk>/', FavoriteDeleteView.as_view(), name='favorite-delete'),
    path('login/', LoginView.as_view(), name='login'),
]
