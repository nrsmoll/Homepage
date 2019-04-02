from django.urls import path

from machinelearn import views

urlpatterns = [
    path('ml-learn/mlCPET', views.mlcpet_calc, name='mlcpet_calc'),
    path('ml-learn/mlCPET_results/', views.mlcpet_calc, name='mlcpet_results'),
    path('ml-learn/mlDASI', views.mldasi_calc, name='mldasi_calc'),
    path('ml-learn/mlDASI_results/', views.mldasi_calc, name='mldasi_results'),
]
