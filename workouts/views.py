from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Workout


# ---------- DASHBOARD ----------
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/dashboard.html', {'workouts': workouts})


# ---------- WORKOUT DETAIL ----------
def workout_detail(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    workout = get_object_or_404(Workout, id=id)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})


# ---------- REGISTER ----------
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Account created! Please log in.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'workouts/register.html')


# ---------- LOGIN ----------
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'workouts/login.html')


# ---------- LOGOUT ----------
def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')


# ---------- ADD WORKOUT ----------
def add_workout(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST['name']
        weight = request.POST['weight']
        reps = request.POST['reps']

        Workout.objects.create(
            user=request.user,
            name=name,
            weight=weight,
            reps=reps
        )
        messages.success(request, 'Workout added successfully!')
        return redirect('dashboard')

    return render(request, 'workouts/add_workout.html')


# ---------- EDIT WORKOUT ----------
def edit_workout(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    workout = get_object_or_404(Workout, id=id, user=request.user)

    if request.method == 'POST':
        workout.name = request.POST['name']
        workout.weight = request.POST['weight']
        workout.reps = request.POST['reps']
        workout.save()
        messages.success(request, 'Workout updated successfully!')
        return redirect('dashboard')

    return render(request, 'workouts/edit_workout.html', {'workout': workout})
    # ---------- DELETE WORKOUT ----------
def delete_workout(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    workout = get_object_or_404(Workout, id=id, user=request.user)

    if request.method == 'POST':
        workout.delete()
        messages.success(request, 'Workout deleted successfully!')
        return redirect('dashboard')

    return render(request, 'workouts/delete_workout.html', {'workout': workout})

