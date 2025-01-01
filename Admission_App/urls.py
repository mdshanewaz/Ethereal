from django.urls import path
from Admission_App import views

app_name = 'Admission_App'

urlpatterns = [
    path('notice/', views.admission_notice_view, name='notice'),
    path('process/', views.admission_process_view, name='process'),
]
