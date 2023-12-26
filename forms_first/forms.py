from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="User Name")
    # email = forms.EmailField()
    # CHOICES=[('s', 'small'), ('m', 'Medium'),('L', 'large')]
    # size=forms.ChoiceField(choices=CHOICES)
    file=forms.FileField()