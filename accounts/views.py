from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import Account


def register(request):
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            first_name = forms.cleaned_data['first_name']
            last_name = forms.cleaned_data['last_name']
            email = forms.cleaned_data['email']
            phone = forms.cleaned_data['phone']
            password = forms.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                               email=email, password=password)
            user.phone = phone
            user.save()
            messages.success(request, 'Registration successful.')
            return redirect('register')
    else:
        forms = RegisterForm()

    context = {
        'forms': forms,
    }

    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Success, logged in')

            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')

    return redirect('login')
