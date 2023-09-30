from django import forms

from catalog.models import Product, Version


class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            #field.help_text = 'Some help text for field'


class ProductForm(StyleFromMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        for item in words:
            if item in cleaned_data:
                raise forms.ValidationError('Ошибка, нельзя использовать слова казино, криптовалюта, крипта, биржа, '
                                            'дешево, бесплатно, обман, полиция, радар')
        return cleaned_data

    def clean_descriptions(self):
        cleaned_data = self.cleaned_data.get('descriptions')
        words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        for item in words:
            if item in cleaned_data:
                raise forms.ValidationError('Ошибка, нельзя использовать слова казино, криптовалюта, крипта, биржа, '
                                            'дешево, бесплатно, обман, полиция, радар')
        return cleaned_data


class VersionForm(StyleFromMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
