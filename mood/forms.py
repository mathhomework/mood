from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mood.models import Listener


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField()

    class Meta:
        model = Listener
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
    def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Listener.objects.get(username=username)
        except Listener.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

class MovieForm(forms.Form):
    title = forms.CharField(label = "Title")