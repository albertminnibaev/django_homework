from django import forms

from catalog.models import Product, Version


class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # field.help_text = 'Some help text for field'


class ProductForm(StyleFromMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner',)

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


class ProductFormStaff(StyleFromMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('descriptions', 'category', 'is_published',)

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

    def clean_sign(self):
        product = self.cleaned_data.get('product')
        sign = self.cleaned_data.get('sign')
        if sign:
            for item in Version.objects.all():
                if item.product == product and item.sign:
                    raise forms.ValidationError('Активной может быть только одна версия продукта')
        return sign
