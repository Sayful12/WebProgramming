from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

HOBBIES_CHOICES = (
    ('gaming','GAMING'),
    ('sports', 'SPORTS'),
    ('films','FILMS'),
    ('travel','TRAVEL'),
    ('reading','READING'),
)

class Profile(models.Model):
    email = models.CharField(max_length=200)
    DOB = models.DateField('Date Of Birth')
    gender = models.CharField(max_length=200)
    hobbies = models.CharField(max_length=10, choices=HOBBIES_CHOICES, default='gaming')

    # True if this profile belongs to a Member
    @property
    def has_account(self):
        return hasattr(self, 'account') and self.account is not None

    # Either the username of the Member, or NONE
    @property
    def account_check(self):
        return str(self.account) if self.has_account else 'NONE'

    def __str__(self):
        return self.text + ' (' + self.member_check + ')'

class Account(User):
   profile = models.OneToOneField(
        to=Profile,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
