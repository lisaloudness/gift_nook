from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('ethos/', views.ethos, name='ethos'),
    path('privacy/', views.privacy, name='privacy'),

]
