from django.db import models
from django.urls import reverse
from .unit import Unit


class Member(models.Model):
    HASIC = 'H'
    STARHASIC = 'SH'
    STROJNIK = 'S'
    TECHNIK = 'T'
    VELITEL_D = 'VD'
    ZASVELITEL = 'ZVJ'
    VELITEL_J = 'VJ'
    FUNCTION = [
        (HASIC, 'Hasič'),
        (STARHASIC, 'Starší hasič'),
        (STROJNIK, 'Strojník'),
        (TECHNIK, 'Technik'),
        (VELITEL_D, 'Velitel družstva'),
        (ZASVELITEL, 'Zástupce velitele jednotky'),
        (VELITEL_J, 'Velitel jednotky')
    ]
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    function = models.CharField(choices=FUNCTION, max_length=10)

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)

    image = models.ImageField(upload_to='images/', default='static/images/firefighter.jpg', blank=True, null=True)
    JEDU = 'JD'
    NEJEDU = 'NJ'
    NEZNAMO = 'NZ'
    STATE = [
        (JEDU, 'Jedu'),
        (NEJEDU, 'Nejedu'),
        (NEZNAMO, 'Neznamo')
    ]
    state = models.CharField(max_length=2, choices=STATE, default=NEZNAMO)


    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse("member_list")

# Overwritten save() function to automatically set "unit" value to first Unit object
    def save(self, *args, **kwargs):
        if Unit.objects.exists():
            self.unit = Unit.objects.first()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Člen'
        verbose_name_plural = 'Členové'
