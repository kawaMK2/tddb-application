from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import *
from material import *
from datetime import datetime


class ObjInputForm(forms.ModelForm):

    class Meta:
        model = ObjInput
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'file': forms.FileInput(attrs={
                'class': "form-control",
            }),
        }


class AddForm(forms.Form):
    name = forms.CharField(label="File name", max_length=200, required=False)
    file = forms.FileField(label="upload some .obj file", allow_empty_file=False, required=True)
    date = forms.DateTimeField(label='Added date', initial=datetime.now(), required=False)
    r = forms.IntegerField(label="Red 0 ~ 255", validators=[MinValueValidator(0), MaxValueValidator(255)], required=False, initial=0)
    g = forms.IntegerField(label="Green 0 ~ 255", validators=[MinValueValidator(0), MaxValueValidator(255)], required=False, initial=0)
    b = forms.IntegerField(label="Blue 0 ~ 255", validators=[MinValueValidator(0), MaxValueValidator(255)], required=False, initial=0)
    thickness = forms.FloatField(label="Thickness default: 1.0", max_value=100.0, required=False, initial=1.0)
    height = forms.FloatField(label="Height default: 1.0", max_value=100.0, required=False, initial=1.0)

    layout = Layout('name', 'file', Row('r', 'g', 'b'), Row('thickness', 'height'), 'date')
