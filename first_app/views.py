from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.

def home(request):
    return render(request,'home.html')


def signUP(request):
   if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Successfully Account created')
                form.save()

        else:
            form = forms.RegisterForm()
        return render(request,'signUp.html',{'form':form})
   else:
       return redirect('profile')


def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userPass = form.cleaned_data['password']
                user = authenticate(username=name,password=userPass)

                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile')



def profile(request):
   if  request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.Change_user(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'Successfully Change Your info')
                form.save()
                return redirect('login')
        else:
            form = forms.Change_user(instance=request.user)
        return render(request,'profile.html',{'form':form})
   else:
       return redirect('signUp')



def LogOut(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method=='POST':
           form=PasswordChangeForm(user=request.user, data=request.POST)

           if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'pass_change.html',{'form':form})
    else:
        return redirect('signUp')


# password change without old password

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method=='POST':
           form=SetPasswordForm(user=request.user, data=request.POST)

           if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'pass_change.html',{'form':form})
    else:
        return redirect('signUp')




