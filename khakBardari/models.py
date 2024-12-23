import re

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


def validate_phone(number):
    # if not re.match(pattern=r'^(?:0|\+?98|\+?1)\s?(?:\d\s?){9,11}$', string=number):
    if not re.match(pattern=r'\d{10}', string=number):
        raise ValidationError(message='Ensure this field has 10 characters.')


class Ranande(models.Model):
    ranande_id = models.CharField(max_length=30, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(validators=[validate_phone],max_length=16, blank=True, null=True)
    logo = models.ImageField(upload_to='Driver_logo/',
                             default='Driver_logo/driver_default_logo.png',
                             validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])],
                             null=True, blank=True)
    car_type_name = models.CharField(max_length=50, blank=True, null=True)
    car_id = models.CharField(max_length=20, blank=True, null=True)
