from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from Responder.models import Member
from Responder.forms import MemberCreateForm, MemberUpdateForm


class MemberListView(ListView):
    model = Member
    template_name = "DjangoResponder/member/member_list.html"


class MemberCreateView(CreateView):
    model = Member
    template_name = "DjangoResponder/member/member_create_form.html"
    form_class = MemberCreateForm


class MemberUpdateView(UpdateView):
    model = Member
    template_name = "DjangoResponder/member/member_update_form.html"
    success_url = reverse_lazy("member_list")
    form_class = MemberUpdateForm


class MemberDeleteView(DeleteView):
    model = Member
    template_name = "DjangoResponder/member/member_delete_form.html"
    success_url = reverse_lazy("member_list")
