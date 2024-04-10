from django import forms
from Responder.models import Member


class MemberCreateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["first_name", "last_name", "function", "phone", "email", "image"]


class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["first_name", "last_name", "function", "phone", "email", "image"]
