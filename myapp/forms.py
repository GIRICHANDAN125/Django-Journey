#forms.py
from django import forms
class InputForm2(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField()
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': '2000-01-01','max': '2010-12-31'}))
    gender = forms.ChoiceField(
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        ]
    )
    address = forms.CharField(widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False)
    website = forms.URLField(required=False)
    agree = forms.BooleanField(required=False)

