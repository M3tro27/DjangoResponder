from django import forms
from Responder.models import Machinery


class MachineryCreateForm(forms.ModelForm):
    class Meta:
        model = Machinery
        fields = ["name", "mark", "licence_plate", "call_sign", "image"]


class MachineryUpdateForm(forms.ModelForm):
    class Meta:
        model = Machinery
        fields = ["name", "mark", "licence_plate", "call_sign", "image"]
