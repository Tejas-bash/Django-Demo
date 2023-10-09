from django import forms
from App.models import DemoForm
class demoForm(forms.ModelForm):
    class Meta:
        model = DemoForm
        fields = ['Name']