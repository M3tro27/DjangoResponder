from django.db import models
from django.urls import reverse
from .unit import Unit


class Machinery(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    licence_plate = models.CharField(max_length=10)
    call_sign = models.CharField(max_length=10)
    mark = models.CharField(max_length=5)
    image = models.ImageField(upload_to='images/', default='static/images/firetruck.png', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("machinery_list")

    # Overwritten save() function to automatically set "unit" value to first Unit object
    def save(self, *args, **kwargs):
        if Unit.objects.exists():
            self.unit = Unit.objects.first()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Technika"
        verbose_name_plural = "Technika"
