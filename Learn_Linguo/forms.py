from django import forms
from .models import ReferenceText

class ReferenceTextForm(forms.ModelForm):
    class Meta:
        model = ReferenceText
        fields = ['text']