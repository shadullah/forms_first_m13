from django.shortcuts import render
from . forms import contactForm

# Create your views here.
def home(req):
    return render(req, 'forms_first/home.html')

def about(req):
    return render(req, 'forms_first/about.html')

def login(req):
    print(req.POST)
    if req.method == 'POST':
        name = req.POST.get('username')
        email = req.POST.get('email')
        return render(req, './forms_first/login.html', {'name': name, 'email': email})
    else:
        return render(req, './forms_first/login.html')
    # return render(req, 'forms_first/login.html')

def djangoForms(req):
    form = contactForm(req.POST)
    if form.is_valid():
        print(form.cleaned_data)
        
    return render(req, './forms_first/django_Form.html', {'form': form})