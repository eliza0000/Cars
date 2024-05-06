from django import  forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_name', 'category', 'marka', 'model','price', 'description', 'year', 'type', 'volume', 'image']