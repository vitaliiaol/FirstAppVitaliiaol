from django import forms
from .models import Review


class AddReview(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ['user', 'book']
        widgets = {
            'text': forms.Textarea(attrs={"class": "form-control"}),
            'rating': forms.Select(attrs={"class": "form-control"})
        }