from django import forms
from .models import reg 

class regform(forms.ModelForm):
    class Meta:
        model = reg
        fields = ['name', 'age','email','username','password']
        
        widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'age':forms.NumberInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'password':forms.TextInput(attrs={'class':'form-control'}),
        
    }
        
        
