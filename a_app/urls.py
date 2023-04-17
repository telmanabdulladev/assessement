from django.urls import path, include 
from .import views 
app_name='a_app'
urlpatterns= [
  path('index/',views.index,name='index'),  
  path('exam/',views.exam, name='exam' ), 
  path('signup/',views.signup, name='signup'),
  path('login/', views.Login, name='login'),
  path('logout/',views.Logout, name='logout'),
  path('resource/', views.resource, name='resource'),
  path('form/',views.forum, name='form')
]






