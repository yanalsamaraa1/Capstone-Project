from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('workout/<int:workout_id>/', views.workout_detail, name='workout_detail'),
]
