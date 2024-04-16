from django import forms

from .models import *
from django.utils.translation import ugettext_lazy as _

import datetime
#from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import SelectDateWidget
from django.forms import ModelForm, Form, DateInput
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget






class DocumentForm(forms.ModelForm):
     class Meta:
        model = Document
        fields = ['photo', 'full_name', 'phone', 'address', 'title', 'cv']
        widgets = {
           # 'photo': forms.ImageField(**options),
            'full_name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'address': forms.TextInput(attrs={'placeholder': 'address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'title': forms.TextInput(attrs={'placeholder': 'Position your applying'}),
            #'cv': forms.FileField(attrs={'placeholder': 'please upload you CV'}),
           
        }
        labels ={
           # 'photo': _(""),
            'full_name': _(""),
            'phone': _(""),
            'address': _(""),
            'title': _(""),
          #  'cv': _(""),
           
        }




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        
        fields = ['from_email', 'phone', 'subject', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'from_email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'message': forms.Textarea(attrs={'placeholder': '\t\tMessage'}),
           
        }
        labels ={
            'subject': _(""),
            'from_email': _(""),
            'phone': _(""),
            'message': _(""),
           
        }


def email(self):
        email = self.cleaned_data.get("subject")
        return email

def name(self):
        name = self.cleaned_data.get("from_email")
        return name

def name(self):
        phone = self.cleaned_data.get("phone")
        return phone

def content(self):
        content = self.cleaned_data.get("message")
        return content
