from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import django.contrib.auth
# Create your views here.


# def loginpage(request):
#     if request.method == "POST":
#         usern = request.POST.get('username')
#         # these are the names of the fields in the html form
#         userpass = request.POST.get('password')

#         user = authenticate(request, username=usern, password=userpass)
#         if user is not None:
#             login(request, user)
#             return redirect('blog-home')
#         else:
#             messages.info(request, 'there is something wrong')

#     return render(request, 'users/login.html')


# def logoutuser(request):

#     logout(request)
#     return redirect('login')
#


def signup(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # to get username from form
            user = form.cleaned_data.get('username')
            messages.success(request, f'account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'users/signup.html', context)


@login_required(login_url='login')
def profile(request):
    return render(request, 'users/profile.html')


def start(request):
    if request.user.is_authenticated:
        return redirect('blog-home')
    else:
        return redirect('login')


@login_required
def profile(request):
    return render(request, 'users/profile.html')
