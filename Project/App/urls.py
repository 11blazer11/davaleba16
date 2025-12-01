from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name='Q&F_lookups'),
]