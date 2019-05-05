from django import forms
from .models import list

class listform(forms.ModelForm):
    class Meta:
        model = list
        fields = ["item","completed"]
