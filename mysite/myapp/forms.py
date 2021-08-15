from django import forms
from .models import Products,Product_Images

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name','price','description', 'category_id')
        labels={
            'name':'Full Name',
            'price':'Price',
            'category_id': 'Category',
            'description':'Description',
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category_id'].empty_label = '--- select option ---'
