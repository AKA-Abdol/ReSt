from django.urls import path 
from . import views

urlpatterns = [
    path('', views.get_all_realties, name='all'),
    path('create/', views.create_realty, name='create')
]