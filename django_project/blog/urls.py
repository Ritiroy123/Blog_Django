from django.urls import path
from .  import views


urlpatterns = [
    path('home/', views.first_program, name='home_page'),
    path('about/', views.about, name='about_page'),
    
]