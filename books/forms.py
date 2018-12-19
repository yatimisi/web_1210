from django import forms

class BookForm(forms.Form):
    name = forms.CharField(max_length=20, label="書名")
    price = forms.IntegerField(min_value=1, label='價格')
    introduction = forms.CharField(widget=forms.Textarea(), label='introduction')