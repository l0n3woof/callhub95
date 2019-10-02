from django.urls import path
from .views import Fibresp

urlpatterns = [
    path('fibnum', Fibresp.as_view(), name='fibo number'),
]
