from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

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

            # USER ACTIVATION
            current_site = get_current_site(request)
            mail_subject = 'Please Activate Your Account'
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            # messages.success(request, 'Thank you for registering with us. We have send you a verification email.')
            return redirect('/account/login/?command=verification&email=' + email)
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

            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')

    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your Account is Activated.')
        return redirect('login')

    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password Reset Email Has been to your email address')
            return redirect('login')

        else:
            messages.error(request, 'Account does not exists.')
            return redirect('forgotpassword')

    return render(request, 'accounts/forgotpassword.html')


def resetpassword_validate(request, uidb64, token):

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')

        return redirect('resetPassword')

    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')




def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confrim_password = request.POST['confrim_password']

        if password == confrim_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()

            messages.success(request, 'Password reset success')
            return redirect('login')

        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:

        return render(request, 'accounts/resetpassword.html')
