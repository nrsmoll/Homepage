from django.urls import path

from . import views

urlpatterns = [
    path('logbook/', views.index, name='index'),
    path('logbook_index/', views.logbook_index, name='logbook_index'),
    path('publications/', views.publications, name='publications'),
]