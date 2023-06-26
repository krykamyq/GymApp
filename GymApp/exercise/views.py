from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import ExerciseForm,ExerciseAdd,TraningForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request , "home.html")


@login_required(login_url='login')
def tranings(request):
    tranings = Traning.objects.filter(user = request.user)

    context ={'tranings': tranings}
    return render(request, 'traning.html',context)

def traning(request, pk):
    traning = Traning.objects.get(id=pk)
    context = {'traning':traning}
    return render(request, 'traningg.html', context)

def deleteExerciseFromTrening(request,pk,pm):
    rep = Reps.objects.get(id= pm)
    if request.method == 'POST':
        rep.delete()
        return redirect('traning',pk)


def deleteTrening(request,pk):
    traning= Traning.objects.get(id= pk)
    if request.method == 'POST':
        traning.delete()
        return redirect('tranings')
    
def addWorkout(request):
    page = 'createworkout'

    if request.method == 'POST':
        form = TraningForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            traning = form.save()
            return redirect('traning', traning.id)
    else:
        form = TraningForm()
    
    context = {'page': page, 'form': form}
    return render(request, 'addcreate.html', context)
    
@login_required(login_url='login')
def addExercise(request,pk):
    page = 'add'
    
    reps = Exercise.objects.all()
    traning = Traning.objects.get(id = pk)
    if request.method == 'POST':
        form = ExerciseAdd(request.POST)
        if form.is_valid():
            reps = form.save()
            traning.workout.add(reps)
            return redirect('traning', pk)
    else:
        form = ExerciseAdd()
    
    context = {'form': form, 'page': page}
    return render(request, 'addcreate.html', context)

    
def exercise(request):
    exercises = Exercise.objects.filter(isAccepted=True)

    context = {'exercises': exercises}
    return render(request, 'exercise.html', context)
 
@login_required(login_url='login')
def create_exercise(request):
    page = 'create'
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save()
            return redirect('exercise')
    else:
        form = ExerciseForm()
    
    context = {'form': form, 'page': page}
    return render(request, 'addcreate.html', context)

def login_page(request):

    page = 'login'
    context = {'page': page}
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
        except:
            messages.error(request, 'User does not exist.')

        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name for the home page
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html',context)
    
    return render(request, 'login.html', context)
    
   
def registration_page(request):
    page = 'registration'
    context = {'page': page}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists.')
                return render(request, 'login.html',context)
            else:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('home')  # Replace 'home' with the URL name for the home page
        else:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'login.html',context)
    
    return render(request, 'login.html',context)

    
    

def logout_user(request):
     logout(request)
     return redirect('home')