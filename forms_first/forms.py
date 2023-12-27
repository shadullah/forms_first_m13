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
    # def clean_name(self):
    #     valName = self.cleaned_data['name']
    #     if len(valName) < 10:
    #         raise forms.ValidationError("Enter 10 characters")
    #     return valName

    def clean(self):
        cleaned_data = super().clean()
        valname=self.cleaned_data['name']
        valemail=self.cleaned_data['email']
        if len(valname) < 10:
            raise forms.ValidationError("Enter 10 characters")
        if '.com' not in valemail:
            raise forms.ValidationError("email must contain .com")


# forms validators
def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("Enter a value above 10 character")

class testing(forms.Form):
    name=forms.CharField(widget=forms.TextInput, validators=[len_check])


#password matching project
    
class passwordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data= super().clean()
        val_name=self.cleaned_data['name']
        val_pass= self.cleaned_data['password']
        val_confirm_pass= self.cleaned_data['confirm_password']
        if val_confirm_pass!=val_pass:
            raise forms.ValidationError("password doesn't match")
        if len(val_name)<8:
            raise forms.ValidationError("name must be greater of 8 characters")
