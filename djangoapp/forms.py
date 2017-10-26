from django import forms
from . import models


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
        exclude = ['preview']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = '__all__'