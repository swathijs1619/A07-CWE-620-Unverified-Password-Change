from django.shortcuts import render, redirect, reverse

# Using the default user model
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        last = request.POST.get('last')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User()
        user.first_name = name
        user.last_name = last
        user.username = email
        user.email = email
        user.save()

        user.set_password(password)
        user.save()

        messages.success(request, "Signup success!!")

        return redirect(
            reverse('signup')
        )


    else:
        return render(
            request,
            "signup.html",
            {
                'title': 'Signup'
            }
        )
