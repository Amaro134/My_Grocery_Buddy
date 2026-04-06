from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'quantity', 'category', 'price', 'complete']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'complete': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
