"""Store application forms and formsets."""

from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """Form for product in the store."""

    model = Product
    fields = ('article', 'name', 'category', 'price', 'cost', 'count', 'store', 'is_active')
    widgets = {
        'article': forms.TextInput(
            attrs={'placeholder': 'Article'},
        ),
        'name': forms.TextInput(
            attrs={'placeholder': 'Name'},
        ),
        'price': forms.NumberInput(
            attrs={'placeholder': 'Price'},
        ),
        'cost': forms.NumberInput(
            attrs={'placeholder': 'Cost'},
        ),
        'count': forms.NumberInput(
            attrs={'placeholder': 'Count'},
        ),
    }

# Formset for products based on `ProductForm` class
ProductFormSet = forms.modelformset_factory(
    model=Product,
    form=ProductForm,
    fields=ProductForm.fields,
    widgets=ProductForm.widgets,
)
