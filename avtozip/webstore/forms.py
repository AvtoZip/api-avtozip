"""WebStore application forms and formsets."""

from django import forms

from .models import Product


class BaseModelForm(forms.ModelForm):
    """Base model form with common logic."""

    def __init__(self, *args, **kwargs):
        """Base constructor to initialize common attributes."""
        for field_name, input in self.widgets.items():
            input.attrs['placeholder'] = self.model._meta.get_field(field_name).verbose_name
        super(BaseModelForm, self).__init__(*args, **kwargs)


class ProductForm(BaseModelForm):
    """Form for product in the storeBaseModelForm."""

    model = Product
    fields = ('article', 'name', 'category', 'price', 'cost', 'count', 'store', 'is_active')
    widgets = {
        'article': forms.TextInput(),
        'name': forms.TextInput(),
        'price': forms.NumberInput(),
        'cost': forms.NumberInput(),
        'count': forms.NumberInput(),
    }

# Formset for products based on `ProductForm` class
ProductFormSet = forms.modelformset_factory(
    model=Product,
    form=ProductForm,
    fields=ProductForm.fields,
    widgets=ProductForm.widgets,
)
