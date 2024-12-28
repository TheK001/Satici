from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class" : "form-control"}
    ))
    cost = forms.FloatField(widget=forms.NumberInput(
        attrs={"class" : "form-control"}
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={"class" : "form-control"}
    ))
    image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={"class" : "form-control"}
    ))
    class Meta():
        model = Product
        fields = ["name", "cost", "description", "image"]


