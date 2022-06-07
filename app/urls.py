from django.urls import path, include
from .views import Home,send_files




urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('upload', send_files.as_view(), name="uploads")
]