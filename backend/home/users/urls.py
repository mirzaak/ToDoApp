from django.urls import path
from .views import RegisterAPI, UserData

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('user/', UserData.as_view(), name='user'),
]