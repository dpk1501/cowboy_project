from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def info1(request):
    return render(request, 'main/info1.html')

def info2(request):
    return render(request, 'main/info2.html')

def index(request):
    return render(request, 'main/index.html')
