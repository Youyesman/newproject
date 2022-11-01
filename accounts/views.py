from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request,username= username, password=password)
        if user is not None : 
            auth.login(request, user)
            return redirect('/')
        else : 
            return redirect('/accounts/login')
    else:
        return render(request,'login.html')
    
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('/accounts/login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            password=password,
        )
        user.save()
        return redirect('/accounts/login')
    else:
        return render(request,'signup.html')
    