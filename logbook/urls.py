from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logbook/', views.logbook_index, name='logbook_index'),
    path('publications/', views.publications, name='publications'),
]