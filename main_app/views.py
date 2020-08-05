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

def signup(request):
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

def update(request, user):
    user = Profile.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_id = request.user_id
            user.save()
            return redirect('profile', user.user_id)

# def update(request):
#   if request.method == 'POST':
#     name = request.POST['name']
#     city = request.POST['breed']
#     form = ProfileForm(request.POST)
#     new_profile = form.save(commit=false)
#     new_profile.user = request.user
#     new_profile.save()
#     return redirect('detail', new_profile.id)
#   else:
#     form = ProfileForm()
#     return render(request, 'profile.html')

def profile(request, user_id):
    # profile = Profile.objects.get()
    return render(request, 'profile.html')