from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from a_app.models import  Resource, Comment, Exam,Forum, Account
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.

def index(request):
    context = {
        
    }
    if request.user.is_authenticated:
       resources=Resource.objects.filter(istifadeciler=request.user)
       context['resources'] = resources
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
def resource(request):
    context = {
        
    }
    if request.user.is_authenticated:
        resources=Resource.objects.filter(istifadeciler=request.user)
        context["resources"] = resources
    return render(request,'resource.html',context)

def forum(request):
    context ={
        
    }
    if request.user.is_authenticated:
        forms=Forum.objects.filter(istifadeci=request.user)
        
        context['forms'] = forms
            
        if request.method=="POST":
            choice=request.POST.get("choice")
            if choice=="forum":
                title=request.POST.get("title")
                content=request.POST.get("content")
                category=request.POST.get("category")
                            
                Forum.objects.create(
                   title=title,
                   content=content,
                   category=category,
                   istifadeci=request.user
                )
        
                messages.success(request,"form ugurla yaradildi")
                return redirect("a_app:forum")
            
            elif choice=="comment":
                forum_id=request.POST.get("forum_id")
                comment_content=request.POST.get("comment_content")
                # id-si forum_id-ye beraber olan forumu Forum classindan cekirik
                forum=Forum.objects.get(id=forum_id)
                
                Comment.objects.create(
                    content=comment_content,
                    istifadeci=request.user,
                    forum = forum
                )
        
    return render(request,'forum.html',context)

def resource_detail(request,id):
    context ={
        
    }
    if request.user.is_authenticated:
        resource=Resource.objects.get(id=id)
        # dictionary-ya element elave etmek
        context["resource"] = resource
    return render(request,'detail.html', context)

def exam_detail(request,id):
    context = {
        
    }
    if request.user.is_authenticated:
        exam=Exam.objects.get(id=id)
        context["exam"] = exam
    return render(request,'exam_detail.html',context)
            
        



        

    
    
    
    

