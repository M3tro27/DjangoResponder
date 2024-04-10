from django.db import models
from django.urls import reverse
from Responder.geocoding import get_geocordinates


class Unit(models.Model):
    JPO_I = 'I'
    JPO_II = 'II'
    JPO_III = 'III'
    JPO_IV = 'IV'
    JPO_V = 'V'
    JPO_VI = 'VI'
    UNIT = [
        (JPO_I, 'JPO I'),
        (JPO_II, 'JPO II'),
        (JPO_III, 'JPO III'),
        (JPO_IV, 'JPO IV'),
        (JPO_V, 'JPO V'),
        (JPO_VI, 'JPO VI')
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(choices=UNIT, max_length=10)
    minutes_to_answer = models.IntegerField(default=2)

    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.category

    def get_absolute_url(self):
        return reverse('index')

    def save(self, *args, **kwargs):
        address = f"{self.street}, {self.city}, {self.country}, {self.zipcode}"
        latitude, longitude = get_geocordinates(address)
        if latitude is not None and longitude is not None:
            self.latitude = latitude
            self.longitude = longitude
        if self.category == "I" or self.category == "IV":
            self.minutes_to_answer = 2
        elif self.category == "II":
            self.minutes_to_answer = 5
        else:
            self.minutes_to_answer = 10
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Jednotka'
        verbose_name_plural = 'Jednotky'
