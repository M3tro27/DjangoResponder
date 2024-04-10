from django.db import models
from django.urls import reverse

from .member import Member
from .machinery import Machinery
from .unit import Unit
from Responder.geocoding import get_geocordinates


class Call(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    POZAR = 'P'
    TECHPOM = 'TP'
    DOPNEH = 'DN'
    ZACH = 'ZOZ'
    UNIK = 'UNL'
    INC_TYPE = [
        (POZAR, 'Požár'),
        (TECHPOM, 'Technická pomoc'),
        (DOPNEH, 'Dopravní nehoda'),
        (ZACH, 'Záchrana osob a zvířat'),
        (UNIK, 'Únik nebezpečných látek')
    ]
    inc_type = models.CharField(choices=INC_TYPE, max_length=10)

    NIZBUD = 'NB'
    VYSBUD = 'VB'
    DOPR = 'DP'
    STROM = 'Strom'
    HMYZ = 'Hmyz'
    CERP = 'Cerpani'
    VZDUCH = 'Vzduch'
    VODA = 'Voda'
    PUDA = 'Puda'
    PROST = 'Prostor'
    TRAV = 'Trava'
    INC_SUBTYPE = [
        (NIZBUD, 'Nízké budovy'),
        (VYSBUD, 'Výškové budovy'),
        (DOPR, 'Dopravní prostředek'),
        (STROM, 'Odstranění stromu'),
        (HMYZ, 'Likvidace hmyzu'),
        (CERP, 'Čerpání vody'),
        (VZDUCH, 'Do ovzduší'),
        (VODA, 'Do vody'),
        (PUDA, 'Do půdy'),
        (PROST, 'Uzavřený prostor'),
        (TRAV, 'Polní porost, tráva'),
    ]
    inc_subtype = models.CharField(choices=INC_SUBTYPE, max_length=20)

    date = models.DateField()
    time = models.TimeField()

    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    place_desc = models.CharField(max_length=50)

    inc_desc = models.CharField(max_length=50)
    inc_level = models.IntegerField(default=1)

    members = models.ManyToManyField(Member, blank=True)
    trucks = models.ManyToManyField(Machinery, blank=True)

    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.inc_type + " - " + self.inc_subtype + ", " + self.city

    def save(self, *args, **kwargs):
        if Unit.objects.exists():
            self.unit = Unit.objects.first()
        address = f"{self.address}, {self.city}, Česko"
        latitude, longitude = get_geocordinates(address)
        if latitude is not None and longitude is not None:
            self.latitude = latitude
            self.longitude = longitude
        super().save(*args, **kwargs)

    def call_short_name(self):
        return self.inc_type + " - " + self.inc_subtype

    def call_address(self):
        return self.city + " " + self.address

    def get_absolute_url(self):
        return reverse('call_list')
