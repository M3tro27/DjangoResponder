from django.contrib import admin

# Register your models here.
from Responder.models import Call, Equipment, Machinery, Member, Unit


admin.site.register(Call)
admin.site.register(Equipment)
admin.site.register(Machinery)
admin.site.register(Member)
admin.site.register(Unit)
