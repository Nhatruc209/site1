from django import forms
from .models import Home

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['ten', 'mo_ta', 'tags', 'hinh_anh', 'dia_chi', 'luot_xem', 'status']
      
        widgets = {
            'ten': forms.TextInput(attrs={'class': 'form-control'}),
            'mo_ta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'hinh_anh': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'dia_chi': forms.TextInput(attrs={'class': 'form-control'}),
            'luot_xem': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }