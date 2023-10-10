from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
   
    path('',views.home,name='home'),
    path('project1',views.project1,name='project1'),
    path('project2',views.project2,name='project2'),
    path('third',views.third,name='third'),
    
]
