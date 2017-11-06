from django import forms


class OrderForm(forms.Form):
    email = forms.EmailField(required=True, max_length=64)
    name = forms.CharField(required=True, max_length=64)
    surname = forms.CharField(required=True, max_length=64)
    mobile_number = forms.CharField(required=True, max_length=32)
    appendage = forms.CharField(max_length=2048, required=True)
    address = forms.CharField(required=True, max_length=64)


class ProductsForm(forms.Form):
    book_id = forms.CharField(required=True, max_length=64)
    price = forms.CharField(required=True, max_length=64)
    nmb = forms.CharField(required=True, max_length=64)