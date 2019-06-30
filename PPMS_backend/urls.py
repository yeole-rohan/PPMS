from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/',LoginView.as_view(), name='login'),
    path('account/', views.accountForm, name="account"),
    path('account-form/', views.account, name="account-form"),
    path('diesel/', views.dieselStock, name="diesel"),
    path('diesel-form', views.dieselForm, name="diesel-form"),
    path('diesel-nozzle/', views.dieselNozzle, name="diesel-nozzle"),
    path('diesel-nozzle-form/', views.dieselNozzleForm, name="diesel-nozzle-form"),
    path('diesel-density/', views.dieselDensity, name="diesel-density"),
    path('diesel-density-form/', views.dieselDensityForm, name="diesel-density-form"),
    path('petrol-density/', views.petrolDensity, name="petrol-density"),
    path('petrol-density-form/', views.petrolDensityForm, name="petrol-density-form"),
    path('petrol-stock/', views.petrolStock, name="petrol-stock"),
    path('petrol-stock-form/', views.petrolStockForm, name="petrol-stock-form"),
    path('petrol-nozzle/', views.petrolNozzle, name="petrol-nozzle"),
    path('petrol-nozzle-form/', views.petrolNozzleForm, name="petrol-nozzle-form"),
]
