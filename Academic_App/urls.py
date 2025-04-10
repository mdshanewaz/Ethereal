from django.urls import path
from Academic_App import views

app_name = 'Academic_App'

urlpatterns = [
    path('curriculum/', views.curriculum_view, name='curriculum'),
    path('syllabus/', views.syllabus_view, name='syllabus'),
    path('booklist/', views.bookList_view, name='book'),
    path('routine/', views.classSchedule_view, name='routine'),
    path('exam/', views.examSchedule_view, name='exam'),
    path('career/', views.career_view, name='career'),
]
