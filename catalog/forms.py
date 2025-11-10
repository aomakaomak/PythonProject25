from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']
        exclude = ['owner']


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберете категорию',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену',
        })


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


    def clean_price(self):

        price = self.cleaned_data.get('price')

        if price < 0:
            raise ValidationError('Цена не может быть отрицательной!')
        return price
