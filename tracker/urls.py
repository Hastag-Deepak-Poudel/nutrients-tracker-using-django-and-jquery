from django.urls import path
from . import views

app_name = "tracker"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('delete/<int:pk>/', views.delete, name='delete_item')
]