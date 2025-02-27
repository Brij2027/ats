from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class GenderChoices:
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    Choices = (
        (MALE, MALE),
        (FEMALE, FEMALE),
        (OTHER, OTHER)
    )

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(choices=GenderChoices.Choices, default=GenderChoices.MALE, max_length=1)
    email = models.EmailField(null=False)
    phone_number = PhoneNumberField(null=False)
