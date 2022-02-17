from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('recharge/', views.recharge, name='recharge'),
    path('recharge/paymenthandler/', views.paymenthandler, name='paymenthandler'),
]
