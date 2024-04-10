from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from Responder.models import Equipment
from Responder.forms import EquipmentCreateForm, EquipmentUpdateForm


class EquipmentListView(ListView):
    model = Equipment
    template_name = "DjangoResponder/equipment/equipment_list.html"


class EquipmentCreateView(CreateView):
    model = Equipment
    template_name = "DjangoResponder/equipment/equipment_create_form.html"
    form_class = EquipmentCreateForm


class EquipmentUpdateView(UpdateView):
    model = Equipment
    template_name = "DjangoResponder/equipment/equipment_update_form.html"
    success_url = reverse_lazy("equipment_list")
    form_class = EquipmentUpdateForm


class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = "DjangoResponder/equipment/equipment_delete_form.html"
    success_url = reverse_lazy("equipment_list")
