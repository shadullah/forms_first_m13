from django.shortcuts import render
from . forms import contactForm, studentData, testing,passwordValidation

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
    if req.method=='POST':
        form = contactForm(req.POST, req.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./forms_first/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(req, './forms_first/django_Form.html', {'form': form})
    else:
        form=contactForm()
    return render(req, './forms_first/django_Form.html', {'form': form})

def studentForm(req):
    if req.method=='POST':
        form=studentData(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=studentData()
    return render(req, './forms_first/django_form.html', {'form': form})
    

def testing_validations(req):
    if req.method=='POST':
        form=testing(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=testing()
    return render(req, './forms_first/django_form.html', {'form': form})


def passwordValid(req):
    if req.method=='POST':
        form=passwordValidation(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=passwordValidation()
    return render(req, './forms_first/django_form.html', {'form': form})