from django import forms
from .models import Thing
from django.core.validators import MaxValueValidator, MinValueValidator

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    name = forms.widgets.TextInput()
    description = forms.CharField(max_length=120, widget=forms.TextInput({}))
    quantity =  forms.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )
