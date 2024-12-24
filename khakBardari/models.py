import re

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.timezone import now

# Create your models here.


def validate_phone(number):
    # if not re.match(pattern=r'^(?:0|\+?98|\+?1)\s?(?:\d\s?){9,11}$', string=number):
    if not re.match(pattern=r'\d{10}', string=number):
        raise ValidationError(message='Ensure this field has 10 characters.')


class Ranande(models.Model):
    ranande_id = models.CharField(max_length=30, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(validators=[validate_phone], max_length=16, blank=True, null=True)
    logo = models.ImageField(upload_to='Driver_logo/',
                             default='Driver_logo/driver_default_logo.png',
                             validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])],
                             null=True, blank=True)
    car_type_name = models.CharField(max_length=50, blank=True, null=True)
    car_id = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.first_name


class ServiceKhak(models.Model):
    ranande = models.ForeignKey(Ranande, on_delete=models.PROTECT)
    mohandes = models.ForeignKey(User, on_delete=models.PROTECT)
    maghsad = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(default=now())

    def __str__(self):
        return f'{self.date}'
