from django.urls import path
from About_App import views

app_name = 'Product_App'

urlpatterns = [
    path('', views.about_view, name='home'),
]
