from django import forms

# widgets == field to html input

class contactForm(forms.Form):
    name = forms.CharField(label="User Name", initial='zacky', help_text='total length 5', required=False)
    email = forms.EmailField()
    CHOICES=[('s', 'small'), ('m', 'Medium'),('L', 'large')]
    size=forms.ChoiceField(choices=CHOICES)
    address=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'enter your address'}))
    file=forms.FileField()
    age=forms.CharField(widget=forms.NumberInput)
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))

class studentData(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)