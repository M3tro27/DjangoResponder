from django import forms
from Responder.models import Equipment


class EquipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ["equipment_name", "equipment_type", "equipment_date", "owner", "machinery", "image"]


class EquipmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ["equipment_name", "equipment_type", "equipment_date", "owner", "machinery", "image"]
