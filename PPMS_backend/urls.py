
from django.conf import settings
from django.contrib.auth import logout
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('',include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(next_page= settings.LOGOUT_REDIRECT_URL), name= 'logout'),
    # path('login/',LoginView.as_view(), name='login'),
    path('', views.home, name='home'),

    path('account/', views.account, name="account"),
    path('account-form/', views.accountForm , name="account-form"),
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
    path('petrol-nozzle/petrol-form/', views.petrolNozzleForm, name="form"),
    path('api/res/petrol-profit', views.get_dta ,name="api-data"),
    path('api/res/diesel-profit', views.getDieselProfit ,name="api-datas"),
    path('api/res/petrol-month-sale', views.getPetrolSale, name="petrol-sale")
]
