from django.urls import path
from . import views

app_name = 'password_strength'

urlpatterns = [
    path('', views.password_strength_home, name='password_strength_home'),
    path('result/', views.password_strength_result, name='password_strength_result'),
]
