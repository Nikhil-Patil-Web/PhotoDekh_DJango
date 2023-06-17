from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile

# Create your views here.
def index(request):
    return render(request, 'index.html')


## now we will write a piece of code to register a user by the frontend. 

def signup(request):

    if(request.method=='POST'):
        username =request.POST['username']
        email =request.POST['email']
        password =request.POST['password']
        password2 =request.POST['password2']

        if(password ==password2):
            if User.objects.filter(email =email).exists():
                messages.info(request, 'Email is already present');
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken");
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save();
                return redirect('signup')

        else:
            messages.info(request, 'Passwords Do Not Match')
            return redirect('signup')

    else: 
        return render(request, 'signup.html')
    


def signin(request): 

    if(request.method=="POST"):

        username = request.POST["username"]
        password = request.POST["password"]
        user =auth.authenticate(username=username, password = password);
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Credentials Invalid")
            return redirect('signin')


    else:
        return render(request, 'signin.html')