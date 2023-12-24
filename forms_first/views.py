from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'forms_first/home.html')

def about(req):
    return render(req, 'forms_first/about.html')

def login(req):
    return render(req, 'forms_first/login.html')