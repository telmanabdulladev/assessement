from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from a_app.models import  Resource, Comment, Exam,Form, Account
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.

def index(request):
    resources=Resource.objects.filter(istifadeciler=request.user)
    context={
        'resources': resources
    }
    return render(request, 'index.html',context)

# def exam(request):
#     if request.user.is_authenticated:
        
#       exams=Exam.objects.filter(istifadeciler=request.user)
#       context={
#         'exams':exams,
        
#       }
#     else:
#        messages.info(request,'Login')
#     return render(request, 'exam.html',context)

def signup(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('a_app:signup')
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password=request.POST['password1']
        confirm_password=request.POST['password2']
        father_name=request.POST['father_name']
        category=request.POST['category']
        phone_num=request.POST['phone_num']
        if password!=confirm_password:
            messages.info(request,'password və password təsdqi eyni deyil!')
            return redirect('a_app:signup')
        if not User.objects.filter(username=username).exists():
            user=User.objects.create_user(username=username,email=email,password=password)
            user.first_name=first_name
            user.last_name=last_name
            user.save()
            account=Account.objects.create(istifadeci=user,category=category,father_name=father_name,phone_num=phone_num)
            account.save()
            messages.success(request,'You Logged In')
            return redirect('a_app:index')
            
        else:
            messages.info(request,'Use another username')
    return render(request,'signup.html')

def Login(request):
    if request.user.is_authenticated:
        return redirect('a_app:index')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('a_app:index')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('a_app:index')
        
                   
# @login_required

def exam(request):
    context={}
    if request.user.is_authenticated:
        
      exams = Exam.objects.filter(istifadeciler=request.user)
      context = {'exams': exams}
    return render(request, 'exam.html', context)

    
    
    
    

