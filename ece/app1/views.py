from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def career(request):
    return render(request,"career.html")

def courses(request):
    return render(request,"courses.html")

def Gadgets(request):
    return render(request,"gadgets.html")

def about(request):
    return render(request,"about.html")

