from django.shortcuts import render, redirect
from django.urls import reverse

from Responder.models import Unit, Member, Machinery


def index(request):
    if Unit.objects.exists():
        members = Member.objects.all()
        machinery = Machinery.objects.all()
        return render(request, "DjangoResponder/index.html", {"members": members,
                                                              "machinery": machinery})
    else:
        return redirect(reverse('unitcreate'))
