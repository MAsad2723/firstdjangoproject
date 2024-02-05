from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'home.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')    
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')
def signupUser(request):
    if request.method=="POST":
        username = request.POST.get('username')    
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        print(username, password, email)
        user = User.objects.create_user(username, email, password)
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        return redirect('/')
    return render(request, 'signup.html')
def logoutUser(request):
    logout(request)
    return redirect('/login')