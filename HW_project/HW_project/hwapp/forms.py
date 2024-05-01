import datetime

from django import forms
from django.forms import ModelForm

from .models import Product


class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField(min_value=0)
    quantity = forms.IntegerField(min_value=0)
    added_date = forms.DateField(initial=datetime.date.today,widget=forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))

class ImageForm(forms.Form):
    image = forms.ImageField()



class ChoiceForm(forms.ModelForm):
    # product = forms.ModelChoiceField(queryset=Product.objects.all().values_list('product_name', flat=True))
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'quantity', 'added_date']
