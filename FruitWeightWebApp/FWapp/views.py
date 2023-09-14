from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # For verifying the user's given login info
from django.contrib.auth import authenticate , login , logout  # For user autentification (login/logout)
from django.contrib import messages  # For error flash messages
from .forms import RegistrationForm #default django Registration form

# Create your views here.

def home(request):
    return render(request, "home.html")

def detection(request):
    return render(request, "detection.html")

def loginPage(request):
    page = 'login'
    # Collecting login information given by the user
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        # if the user does not exist:
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

            # if the user exists:
        user = authenticate(request, username=username, password=password)  # We verify his login infos

        # if the infos are correct we log the user in and create a session:
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')

        else:
            messages.error(request, 'Incorrect username or password')
    context = {'page': page}
    return render(request,"login.html",context)

#user registration
def registerPage(request):
    form = RegistrationForm()  # using the django generated registration form
    if request.method == 'POST':  # we collect the user's given data

        form = RegistrationForm(request.POST)  # we pass it to the creation form

        if form.is_valid():  # we verify if the form is valid
            user = form.save(commit=False)
            user.username = user.username.lower()  # we lower the user's username
            user.save()  # we save the user
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # we log the user in
            return redirect(
                'index')  # redirecting the user to the form page to either complete his registration or skip it for later

        else:
            messages.error(request, 'An error occurred during your registration. Please try again.')
    context = {'form': form}

    return render(request, 'login.html',context)

#user logout
def logoutUser(request):
    logout(request)
    return redirect('home')