from django import forms


class CpetForm(forms.Form):
    firstname = forms.CharField(label='First name', max_length=100)
    lastname = forms.CharField(label='Last name', max_length=100)
    age = forms.IntegerField(label='Age', max_value=110, min_value=0)
    bmi = forms.IntegerField(label='BMI', max_value=110, min_value=10)
    chronotropic = forms.IntegerField(label='Chronotropic Response', max_value=200, min_value=0)
    etco2 = forms.IntegerField(label='End-Tidal CO2', max_value=200, min_value=0)
