import django


from django import forms
from .models import Persona

class Personaform(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'