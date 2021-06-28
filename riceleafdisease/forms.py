

from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import User
from django import forms

from .models import *
from crispy_forms.helper import FormHelper


class image_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(image_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False


    class Meta:
        model = Training
        fields = ['disease','image']
        widgets = {'disease':forms.HiddenInput()}