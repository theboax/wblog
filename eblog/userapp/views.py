from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UserProfileForm
from .models import UserProfile, Quote
import random

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # messages.success(request, "You have registered successfully...!!!")
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form':form})



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "You have been logged in!!")
            return redirect('home')
        else:
            messages.error(request, "There was an error trying to login")
            return redirect('login')
    
    return render(request, 'registration/login.html', {})



def logout_user(request):
    logout(request)
    return render(request, 'registration/logout.html')



# @login_required
# def profile_view(request):
#     user_profile = request.user.userprofile
#     return render(request, 'registration/profile.html', {'user_profile': user_profile})


@login_required
def profile_view(request):
    # Get the user's profile (you should adapt this to your actual retrieval method)
    user_profile = UserProfile.objects.get(user=request.user)

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'registration/profile.html', context)
    # try:
    #     user_profile = UserProfile.objects.get(user=request.user)
    # except UserProfile.DoesNotExist:
    #     user_profile = None  # Handle the case where UserProfile doesn't exist
    
    # return render(request, 'registration/profile.html', {'user_profile': user_profile,})



def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'registration/edit_profile.html', {'form': form})




# @login_required
# def edit_profile(request):
#     user_profile = request.user.userprofile
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = UserProfileForm(instance=user_profile)
#     return render(request, 'edit_profile.html', {'form': form})



def display_quotes(request):
    quotes = Quote.objects.all()
    random_quote = random.choice(quotes) if quotes else None
    return render(request, 'registration/quotes.html', {'quote': random_quote})
