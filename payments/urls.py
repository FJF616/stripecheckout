from django.conf.urls import url
from . import views

urlpatterns = [
    url('charge/', views.charge, name='charge'),
    url('', views.HomePageView.as_view(), name='home'),
]