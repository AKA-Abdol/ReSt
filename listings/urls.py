from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_listings, name='all_listings'),
]