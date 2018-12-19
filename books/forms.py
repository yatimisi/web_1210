from django import forms

from .models import Book

#class BookForm(forms.Form):
#    name = forms.CharField(max_length=20, label="書名")
#    price = forms.IntegerField(min_value=1, label='價格')
#    introduction = forms.CharField(widget=forms.Textarea(), label='introduction')

class BookForm(forms.ModelForm):
    class Meta: # 從外部資料尋找
        model = Book
        #fields = ('name', 'introduction')
        fields = '__all__'