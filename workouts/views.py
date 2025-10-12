from django.shortcuts import render, get_object_or_404
from .models import Workout

def dashboard(request):
    workouts = Workout.objects.all().order_by('-date')
    return render(request, 'workouts/dashboard.html', {'workouts': workouts})

def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})
