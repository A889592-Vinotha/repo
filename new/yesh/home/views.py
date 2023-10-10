from django.shortcuts import render

def home(request): 
    return render(request,'home.html')

def project1(request): 
    return render(request,'project1.html')

def project2(request): 
    return render(request,'project2.html')

def third(request): 
    return render(request,'3d.html')
