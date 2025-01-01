from django.urls import path
from About_App import views

app_name = 'About_App'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('feature/', views.feature_view, name='feature'),
    path('faculty/', views.teacher_view, name='faculty'),
    path('extracurr/', views.extracurr_view, name='extracurr'),
    path('campus/', views.resourceful_campus_view, name='campus'),
    path('hifz/', views.hifz_view, name='hifz'),
]
