from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django import forms
from django.contrib.auth.models import User

# Create your views here.

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='أدخل بريدك الإلكتروني.')

    class Meta:
        model = User
        fields = ("username", "email", "password1",)       

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('index')  # أو 'home' حسب ما يناسبك
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# def signup(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():  # التحقق من صحة البيانات قبل الحفظ
#             user = form.save()
#             login(request, user)
#             return redirect('/index')  # استخدم المسار الصحيح
#     return render(request, 'signup.html', {'form': form})



# def home(request):
#        return render(request,'index.html')




