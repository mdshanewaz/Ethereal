from django.urls import path
from About_App import views

app_name = 'About_App'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('feature/', views.feature_view, name='feature'),
]
