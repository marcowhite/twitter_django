from django import forms

from .models import  JitterProfile

class JitterProfileForm(forms.ModelForm):
    class Meta:
        model = JitterProfile
        fields = ('avatar',)