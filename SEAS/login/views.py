from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if 'login' in request.POST:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home/')
            else:
                messages.info(request, 'Invalid Credentials!')
                return redirect('/')
        # elif ('register' in request.POST):
        #     if username == '' or password == '':
        #         messages.error(
        #             request, 'Please provide both username and password')
        #         return redirect('/')
        #     else:
        #         if User.objects.filter(username=username).exists():
        #             messages.info(request, 'Username Already Taken!')
        #             return redirect('/')
        #         else:
        #             user = User.objects.create_user(
        #                 username=username, password=password)
        #             user.save()
        #             messages.info(
        #                 request, 'Account Registered! Please Login Now')
        #             return redirect('/')
    else:
        return render(request, 'login/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Logged Out Successfully!')
    return index(request)
