from .views import RegisterView
from django.urls import path
routes = [
    (r'register',RegisterView),
]