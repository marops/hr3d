from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.core.mail import send_mail
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            emails = []
            for u in User.objects.filter(is_staff=True):
                emails.append(u.email)

            send_mail(
                'HR3D Signup',
                'New user has signed up at HR3D.',
                'noreply@hr3d.leidos.com',
                emails,
                fail_silently=False,
            )

            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})