from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # For verifying the user's given login info
from django.contrib.auth import authenticate , login , logout  # For user autentification (login/logout)
from django.contrib import messages  # For error flash messages
from .forms import RegistrationForm, UploadFileForm #default django Registration form & file upload form
import os
from django.conf import settings  # Import Django settings
from .Detection import pictureDetection, videoDetection




# home page
def home(request):
    return render(request, "home.html")




#login page
def loginPage(request):
    if  request.user.is_authenticated:
        return redirect('home')
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
    if  request.user.is_authenticated:
        return redirect('home')

    form = RegistrationForm()  # using the django generated registration form
    if request.method == 'POST':  # we collect the user's given data

        form = RegistrationForm(request.POST)  # we pass it to the creation form

        if form.is_valid():  # we verify if the form is valid
            user = form.save(commit=False)
            user.username = user.username.lower()  # we lower the user's username
            user.save()  # we save the user
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # we log the user in
            return redirect('index')  # redirecting the user to the form page to either complete his registration or skip it for later

        else:
            messages.error(request, 'An error occurred during your registration. Please try again.')
    context = {'form': form}

    return render(request, 'login.html',context)

#user logout
def logoutUser(request):
    logout(request)
    return redirect('home')




def detection(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']

            # Construct the absolute path to the directory where you want to save files
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'UploadedFiles')

            # Create the directory if it doesn't exist
            os.makedirs(upload_dir, exist_ok=True)

            # Construct the full file path
            file_path = os.path.join(upload_dir, uploaded_file.name)

            # Save the uploaded file to a specific location
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)



            # Perform object detection using the YOLO model
            if uploaded_file.content_type.startswith('image') :
                pictureDetection(file_path)
            else:
                videoDetection(file_path)

            return redirect('results')# Redirect to the results page
    else:
        form = UploadFileForm()
    context = {'form': form}
    return render(request, 'detection.html', context)



#page where we can display the results
def results(request):
    return render(request, "results.html")










