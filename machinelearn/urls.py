from django.urls import path

from machinelearn import views

urlpatterns = [
    path('ml-learn/', views.mlcpet_calc, name='mlcpet_calc'),
    path('ml-learn/mlCPET_results/', views.mlcpet_calc, name='mlcpet_results'),
]
