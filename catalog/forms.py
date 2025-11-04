from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not email.endswith('@example.com'):
            raise ValidationError('Email должен оканчиваться на @example.com')
        return email
