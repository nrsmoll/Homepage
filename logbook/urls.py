from django.urls import path

from . import views

urlpatterns = [
    path('logbook/', views.index, name='index'),
    path('logbook_index/', views.logbook_index, name='logbook_index'),
    path('publications/', views.publications, name='publications'),
    path('logbook/create/', views.ConsultationCreate.as_view(), name='consultation_create'),
    path('logbook/<int:pk>/update/', views.ConsultationUpdate.as_view(), name='consultation_update'),
    path('logbook/<int:pk>/delete/', views.ConsultationDelete.as_view(), name='consultation_delete'),
]