from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import  login_required
from .forms import ProfileForm
from listing.models import Property
from django.http import HttpResponse
@login_required
def profile_update(request):
    profile = request.user.profile
    print(profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            profile_picture = form.cleaned_data['profile_picture']
            obj = User.objects.get(username=request.user.username)
            obj.first_name = first_name
            obj.last_name = last_name
            obj.save()
            obj1 = Profile.objects.get(user=request.user)
            obj1.phone_number = phone_number
            obj1.address = address
            obj1.profile_picture=profile_picture
            obj1.save()
            return redirect('profile')
    else:
        form = ProfileForm()
        
    return render(request, 'profile_form.html', {'form': form, 'profile':profile})


def sign_in(request):
    messages.error(request,f'')
    messages.success(request,f'')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        
        form = LoginForm()
        return render(request,'login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('profile')
        
        # either form not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')

@login_required
def profile(request):
    user = request.user
    prof = Profile.objects.get(user=user)
    wishs = []
    for i in prof.wishlist:
        prop = Property.objects.get(id=i)
        wishs.append(prop)
    return render(request,'profile.html',{'user': user, 'prof':prof, 'wishs':wishs})

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'sign_up.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            prof = Profile.objects.create(user=user)
            prof.save()
            return redirect('profile')
        else:
            return render(request, 'sign_up.html', {'form': form})

    