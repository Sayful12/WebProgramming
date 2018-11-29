from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Account(User):
   profile = models.OneToOneField(
        to=Profile,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
     = models.ManyToManyField(
        to='self'   ,
        blank=True,
        symmetrical=False
    )
    messages = models.ManyToManyField(
        to='self',
        blank=True,
        symmetrical=False,
        through='Message',
        related_name='related_to'
    )

class Profile(models.Model):
    email = models.CharField(max_length=200)
    DOB = models.DateField('Date Of Birth')
    gender = models.CharField(max_length=200)
    hobbies = models.TextField()
	
    # True if this profile belongs to a Member
    @property
    def has_member(self):
        return hasattr(self, 'member') and self.member is not None

    # Either the username of the Member, or NONE
    @property
    def member_check(self):
        return str(self.member) if self.has_member else 'NONE'

    def __str__(self):
        return self.text + ' (' + self.member_check + ')'