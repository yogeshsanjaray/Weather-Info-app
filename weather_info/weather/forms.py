from django import forms
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name' : forms.TextInput(attrs={'type':'text','class':'form-control',' placeholder':'City Name','aria-describedby':'basic-addon2'})
        }



