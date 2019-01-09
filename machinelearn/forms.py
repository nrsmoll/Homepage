from django import forms


class CpetForm(forms.Form):
    firstname = forms.CharField(label='First name', max_length=100)
    lastname = forms.CharField(label='Last name', max_length=100)
    age = forms.CharField(label='Age', max_length=5)
    bmi = forms.CharField(label='BMI', max_length=5)
    chronotropic = forms.CharField(label='Chronotropic Response', max_length=5)
    etco2 = forms.CharField(label='End-Tidal CO2', max_length=5)
