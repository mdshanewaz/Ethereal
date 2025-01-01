from django.urls import path
from Academic_App import views

app_name = 'Academic_App'

urlpatterns = [
    path('curriculum/', views.curriculum_view, name='curriculum'),
    path('syllabus/', views.syllabus_view, name='syllabus'),
]
