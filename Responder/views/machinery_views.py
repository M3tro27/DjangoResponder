from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from Responder.models import Machinery
from Responder.forms import MachineryCreateForm, MachineryUpdateForm


class MachineryListView(ListView):
    model = Machinery
    template_name = "DjangoResponder/machinery/machinery_list.html"


class MachineryCreateView(CreateView):
    model = Machinery
    template_name = "DjangoResponder/machinery/machinery_create_form.html"
    form_class = MachineryCreateForm


class MachineryUpdateView(UpdateView):
    model = Machinery
    template_name = "DjangoResponder/machinery/machinery_update_form.html"
    success_url = reverse_lazy("machinery_list")
    form_class = MachineryUpdateForm


class MachineryDeleteView(DeleteView):
    model = Machinery
    template_name = "DjangoResponder/machinery/machinery_delete_form.html"
    success_url = reverse_lazy("machinery_list")
