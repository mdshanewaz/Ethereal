from django.urls import path
from about_app import views

app_name = 'about_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('feature/', views.feature_view, name='feature'),
    path('faculty/', views.teacher_view, name='faculty'),
    path('extracurr/', views.extracurr_view, name='extracurr'),
    path('campus/', views.resourceful_campus_view, name='campus'),
    path('hifz/', views.hifz_view, name='hifz'),
    path('contact/', views.contact_view, name='contact'),
    path('thanks/', views.thanks_view, name='thanks'),
]
