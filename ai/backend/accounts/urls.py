from django.urls import path
from .views import RegisterView, LoginView, StudentProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', StudentProfileView.as_view(), name='profile'),
    path('validate/', StudentProfileView.as_view(), name='validate'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]