from django.urls import path, include 
from .import views 
app_name='a_app'
urlpatterns= [
  path('index/',views.index,name='index'),  
  path('exam/',views.exam, name='exam' ), 
  path('signup/',views.signup, name='signup'),
  path('login/', views.login, name='login') 
]






