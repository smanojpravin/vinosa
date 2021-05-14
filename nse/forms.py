from django.core import validators
from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import members,nifty,banknifty


class StudentRegistration(forms.ModelForm):

    class Meta:
        model = members
        fields = ['name','email','membership']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
        }


class NiftyDataForm(forms.ModelForm):

    class Meta:
        model = nifty
        fields = ['signal','entry','target','advisory']
        widgets = {
            'entry' : forms.TextInput(attrs={'type':'number'}),
            'target' : forms.TextInput(attrs={'type':'number'}),
            'advisory' : forms.Textarea(attrs={'class':'form-control'}),
        }



class BankNiftyDataForm(forms.ModelForm):

    class Meta:
        model = banknifty
        fields = ['signal','entry','target','advisory']
        widgets = {
            'entry' : forms.TextInput(attrs={'type':'number'}),
            'target' : forms.TextInput(attrs={'type':'number'}),
            'advisory' : forms.Textarea(attrs={'class':'form-control'}),
        }