from django import forms
from Responder.models import Call


class CallCreateForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ["inc_type", "inc_subtype", "inc_level",
                  "date", "time", "address", "city",
                  "place_desc", "inc_desc",
                  "trucks", "active"]


class CallUpdateForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ["inc_type", "inc_subtype", "inc_level",
                  "date", "time", "address", "city",
                  "place_desc", "inc_desc",
                  "members", "trucks", "active"]
