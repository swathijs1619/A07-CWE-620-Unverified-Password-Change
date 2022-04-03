from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .froms import RegisterForms,EditRegisterForms
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


# Create your views here.

def home(request):
    return render(request,'home/home.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have login")
            return redirect('home')

        else:
            messages.success(request,"try Again")
            return redirect('login')
    else:
        return render(request,'authenticate/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "logout your account ?")
    return redirect('login')


def register_view(request):
    if request.method == "POST":
        form =RegisterForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request,"Register Your Account")
            return redirect('home')

    else:
        form =RegisterForms()
    context = {
        "form":form,
    }
    return render(request,'register/register.html',context)

def edit_register_view(request):
    if request.method == "POST":
        form =EditRegisterForms(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Change Your Profile Data")
            return redirect('home')

    else:
        form =EditRegisterForms(instance = request.user)
    context = {
        "form":form,
    }
    return render(request,'register/edit_register.html',context)


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,"Your Password Change")
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)

    context ={
        'form':form,
    }
    return render(request,'changePassword/changePassword.html',context)


class PasswordReset(PasswordResetView):
    template_name = 'changePassword/passwordReset.html'

class PasswordResetDone(PasswordResetDoneView):
    template_name = 'changePassword/password_reset_done.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'changePassword/password_reset_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'changePassword/password_reset_complete.html'
