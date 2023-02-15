from django import forms
from .models import Apply

class ApplyForm(forms.ModelForm):
    EmailAddress = forms.EmailField()

    class Meta:
        model = Apply
        fields = ("FirstName", "LastName", "EmailAddress","City", "Country")

# we import our model class
# then we create a form class which inherits forms.ModelForm
# then we create a meta class
