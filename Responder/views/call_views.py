from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from Responder.models import Call
from Responder.forms import CallCreateForm, CallUpdateForm


class CallListView(ListView):
    model = Call
    template_name = "DjangoResponder/call/call_list.html"


class CallCreateView(CreateView):
    model = Call
    template_name = "DjangoResponder/call/call_create_form.html"
    form_class = CallCreateForm


class CallUpdateView(UpdateView):
    model = Call
    template_name = "DjangoResponder/call/call_update_form.html"
    form_class = CallUpdateForm


class CallDeleteView(DeleteView):
    model = Call
    template_name = "DjangoResponder/call/call_delete_form.html"
    success_url = reverse_lazy("call_list")
