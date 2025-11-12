from django.urls import path
from academic_app import views

app_name = 'academic_app'

urlpatterns = [
    path('curriculum/', views.curriculum_view, name='curriculum'),
    path('syllabus/', views.syllabus_view, name='syllabus'),
    path('booklist/', views.bookList_view, name='book'),
    path('routine/', views.classSchedule_view, name='routine'),
    path('exam/', views.examSchedule_view, name='exam'),
    path('career/', views.career_view, name='career'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
    path('year_planner', views.year_planner_view, name='year_planner'),
]
