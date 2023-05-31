from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from a_app.models import  Resource, Comment, Exam,Forum, Account, Answer, UserAnswerCard, Result
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login, logout
from django.http import Http404

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
            return redirect('index')
            
        else:
            messages.info(request,'Use another username')
    return render(request,'signup.html')

def Login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('index')
        
                   
# @login_required

def exam(request):
    if not request.user.is_authenticated:
        raise Http404
    context={
        
     }
    if request.user.is_authenticated:
    #   mydata = Exam.objects.filter(name__startswith='P').values()
    #   print(mydata)
      exams = Exam.objects.filter(istifadeciler=request.user)
      context = {'exams': exams}
    #   context["mydata"] = mydata  
    return render(request, 'exam.html', context)
def resource(request):
    if not request.user.is_authenticated:
        raise Http404
    context = {       
    }
    if request.user.is_authenticated:
        resources=Resource.objects.filter(istifadeciler=request.user)
        context["resources"] = resources
    return render(request,'resource.html',context)

def forum(request):
    if not request.user.is_authenticated:
        raise Http404
    context ={    
    }
    if request.user.is_authenticated:
        forms=Forum.objects.filter(istifadeci=request.user)
        
        context['forms'] = forms
            
        if request.method=="POST":
            # egr bir form varsa choice yazmaqa ehtiyac yoxdur
            choice=request.POST.get("choice")
            if choice=="forum":
                title=request.POST.get("title")
                content=request.POST.get("content")
                category=request.POST.get("category")
                
                        #yuxaridaki melumatlardan obyekt yaradir asaqidaki kimi
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
    if not request.user.is_authenticated:
        raise Http404
    context ={
        
    }
    if request.user.is_authenticated:
        resource=Resource.objects.get(id=id)
        # dictionary-ya element elave etmek
        context["resource"] = resource
    return render(request,'detail.html', context)

def exam_detail(request,id):
    if not request.user.is_authenticated:
        raise Http404
    context = {    
    }
    if request.user.is_authenticated:
        exam=Exam.objects.get(id=id)
        # get ile 1 dene, filter ile bir nece , all ile butun obyektleri cekmek olur
        # if UserAnswerCard.objects.filter(istifadeci=request.user,exam = exam).exists():
        if UserAnswerCard.objects.filter(istifadeci=request.user, exam =exam).exists():
           useranswercard = UserAnswerCard.objects.get(
           istifadeci=request.user,
           exam = exam
           )
           context["useranswercard"] = useranswercard
        context["exam"] = exam
        
    return render(request,'exam_detail.html',context)


            
        



        

    
    
    
    

