from django import forms
from .models import Detail

class Page(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'

