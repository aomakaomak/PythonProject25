from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']


    def clean_name(self):

        forbidden_words = {
            'казино', 'криптовалюта', 'крипта', 'биржа',
            'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        }
        name = self.cleaned_data.get('name')

        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError('Запрещенное слово в названии товара!')
        return name

    def clean_description(self):

        forbidden_words = {
            'казино', 'криптовалюта', 'крипта', 'биржа',
            'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        }
        description = self.cleaned_data.get('description')

        for word in forbidden_words:
            if word in description.lower():
                raise ValidationError('Запрещенное слово в описании товара!')
        return description
