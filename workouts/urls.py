from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('workout/<int:id>/', views.workout_detail, name='workout_detail'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # path('add/', views.add_workout, name='add_workout'),
    path('add/',views.WorkoutCreate.as_view(), name='add_workout'),
    path('edit/<int:id>/', views.edit_workout, name='edit_workout'),
    path('delete/<int:id>/', views.delete_workout, name='delete_workout'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('add_exercise/', views.add_exercise, name='add_exercise'),
    

]

