from django import forms
from django.forms import ModelForm

from .models import crud

class crudForm(forms.ModelForm):
    class Meta:
        model = crud
        fields = '__all__'