from django.urls import path
from . import  views
app_name = 'home'

urlpatterns = [
    path('home',views.home_linkedin, name = 'homepage'),
    path('',views.home_login, name = 'login')
]