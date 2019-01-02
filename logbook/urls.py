from django.urls import path

from . import views

urlpatterns = [
    path('logbook/', views.index, name='index'),
    path('', views.logbook_index, name='logbook_index'),
    path('publications/', views.publications, name='publications'),
]