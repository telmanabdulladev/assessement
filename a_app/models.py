from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    CATEGORIES=(
       ('T','Teacher'), 
       ('S','Student'),
    )
    istifadeci=models.OneToOneField(User,on_delete=models.CASCADE,related_name='account')
    category=models.CharField(max_length=256,choices=CATEGORIES)
    father_name=models.CharField(max_length=256)
    phone_num=models.CharField(max_length=50)
    
    class Meta:
        verbose_name='Account'
        verbose_name_plural='Accounts'
        
    def __str__(self):
        return self.istifadeci.first_name + ' ' + self.istifadeci.last_name + ' ' + self.father_name
    
class Resource(models.Model):
    name=models.CharField(max_length=256)
    file=models.FileField(upload_to='posters/',blank=True, null=True)
    url=models.URLField(max_length=512,blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    istifadeciler=models.ManyToManyField(User,related_name='resources')
    
    class Meta:
        verbose_name='Resource'
        verbose_name_plural='Resources'
    
    def __str__(self):
        return self.name

class Exam(models.Model):
    name=models.CharField(max_length=256)
    status=models.BooleanField(default=False)
    start_date=models.DateTimeField()
    duration=models.DurationField(default=0)
    file=models.FileField(upload_to='examfiles/')
    file_type=models.CharField(max_length=256)
    istifadeciler=models.ManyToManyField(User, related_name='exams')
   
    class Meta:
        verbose_name='Exam'
        verbose_name_plural='Exams'
        
    def __str__(self):
        return self.name
    

class Form(models.Model):
    CATEGORIES=(
       ('Q','Question'), 
       ('I','Information'),
    )
    title=models.CharField(max_length=256)
    category=models.CharField(max_length=1,choices=CATEGORIES)
    content=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    istifadeci=models.ForeignKey(User, on_delete=models.CASCADE, related_name='forms')
    
    def __str__(self):
            return self.name

class Comment(models.Model):
    content=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    istifadeci=models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_comments')
    form=models.ForeignKey(Form,on_delete=models.CASCADE, related_name='form_comments')
    
    def __str__(self):
         return self.name
    


class Question(models.Model):
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE, related_name='questions')
    name=models.CharField(max_length=256)
        
    def __str__(self):
        return self.name
    
    

