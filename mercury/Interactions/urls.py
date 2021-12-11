from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_interaction, name='get_interactions'),
    path('create/', views.add_interaction, name='add_interaction'),
]