from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class BuyCarForm(forms.Form):
    pass


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
