from django import forms
from Responder.models import Unit


class UnitCreateForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ["name", "category", "street", "city", "country", "zipcode"]


class UnitUpdateForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ["name", "category", "street", "city", "country", "zipcode"]
