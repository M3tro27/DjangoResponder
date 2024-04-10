from django.db import models
from django.urls import reverse
from Responder.models import *
import datetime


class Equipment(models.Model):
    AGREGAT = 'AG'
    PRILBA = 'PR'
    KABAT = 'KB'
    KALHOTY = 'KA'
    BOTY = 'BT'
    KUKLA = 'KU'
    DYCHAK = 'IDP'
    VEC = 'OP'
    TYPE_CHOICES = [
        (AGREGAT, 'Agregát'),
        (PRILBA, 'Přilba'),
        (KABAT, 'Kabát'),
        (KALHOTY, 'Kalhoty'),
        (BOTY, 'Boty'),
        (KUKLA, 'Kukla'),
        (DYCHAK, 'Dýchycí přístroj'),
        (VEC, 'Ostatní vybavení')
    ]
    equipment_type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    equipment_name = models.CharField(max_length=40)

    equipment_date = models.DateField(default=datetime.date.today)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    owner = models.ForeignKey(Member, blank=True, null=True, on_delete=models.SET_NULL)
    machinery = models.ForeignKey(Machinery, blank=True, null=True, on_delete=models.SET_NULL)

    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.equipment_name

    def get_absolute_url(self):
        return reverse("equipment_list")

# Overwritten save() function to automatically set "unit" value to first Unit object
    def save(self, *args, **kwargs):
        if Unit.objects.exists():
            self.unit = Unit.objects.first()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Vybavení'
        verbose_name_plural = 'Vybavení'
