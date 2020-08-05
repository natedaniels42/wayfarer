from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile
# Create your views here.
def home(request):
    return render(request, 'home.html')

def city_index(request):
    return render(request, 'city/index.html')

<<<<<<< HEAD
def city_detail(request):
    return render(request, 'city/detail.html')

def city_post(request):
    return render(request, 'city/post.html')

def signup(request):
=======
def signup(request, user_id):
>>>>>>> 149c9e8831a26a7a60855e8c0ed7b2c04ac70396
    error_message = 'Error'
    form = UserCreationForm(request.POST)
    context = {
        'form': form,
        'error_message': error_message,
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'registration/update.html', { 'user': user })
        else:
            global error 
            error = 'User account already exists'
            return render(request, 'registration/signup.html', context)
    else:
        return render(request, 'registration/signup.html', context)


<<<<<<< HEAD
=======
def update(request, user_id):
    # profile = Profile.objects.get()
    return render(request, 'profile.html')
>>>>>>> 149c9e8831a26a7a60855e8c0ed7b2c04ac70396


def profile(request, user_id):
    # profile = Profile.objects.get()
    return render(request, 'registration/profile.html')