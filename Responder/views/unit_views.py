from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from Responder.models import Unit
from Responder.forms import UnitCreateForm, UnitUpdateForm


class UnitDetailView(DetailView):
    model = Unit
    template_name = "DjangoResponder/unit/unit_detail.html"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset.first()


class UnitCreateView(CreateView):
    model = Unit
    template_name = "DjangoResponder/unit/unit_create_form.html"
    form_class = UnitCreateForm


class UnitUpdateView(UpdateView):
    model = Unit
    template_name = "DjangoResponder/unit/unit_update_form.html"
    success_url = reverse_lazy("unitdetail")
    form_class = UnitUpdateForm


class UnitDeleteView(DeleteView):
    model = Unit
    template_name = "DjangoResponder/unit/unit_delete_form.html"
    success_url = reverse_lazy("index")
