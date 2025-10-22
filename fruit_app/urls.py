# fruit_app/urls.py
from django.urls import path
from .views import send_fruits, info_fruits

app_name = 'fruit_app' 

urlpatterns = [
    path('', send_fruits),
    path('info/', info_fruits),
]
