# fruit_app/urls.py
from django.urls import path
from .views import send_fruits

app_name = 'fruit_app'  # optional, aber hilfreich

urlpatterns = [
    path('', send_fruits),
]
