from django import forms

from newspaper.models import *


class NewsForm(forms.Form):
    head = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = News
        fields = 'head, text'


class ImageForm(forms.Form):
    image = forms.FileField()

    class Meta:
        model = Image
        fields = 'image'
