from django import forms
from .models import list
from .models import mail_id

class ListForm(forms.ModelForm):
    class Meta:
        model = list
        fields = ["item","completed"]

class MailForm(forms.ModelForm):
    class Meta:
        model = mail_id
        fields = ["mail"]