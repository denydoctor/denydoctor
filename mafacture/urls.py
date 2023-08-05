from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ajouter-client', views.AjouterClientView.as_view(), name='ajouter-client'),
]


