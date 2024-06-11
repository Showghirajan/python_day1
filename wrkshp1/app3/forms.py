from django import forms
from app3.models import Customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['fname','lname','adhar','phone']