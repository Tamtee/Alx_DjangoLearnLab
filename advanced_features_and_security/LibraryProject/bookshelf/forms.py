from django import forms
from .models import Book
from django.core.exceptions import ValidationError
import datetime

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']  # use your real fields

        fields = ["title", "author", "published_date"]

    def clean_published_date(self):
        pd = self.cleaned_data.get("published_date")
        if pd and pd > datetime.date.today():
            raise ValidationError("Published date cannot be in the future.")
        return pd

class SearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=255)
