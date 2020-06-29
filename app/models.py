from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

CULTIVATION_CHOICES = (
    ('Group', 'Group'),
    ('Partnership', 'Partnership'),
    ('Individual','Individual'),
    )
CAPITAL=(
    ('Savings', 'Savings'),
    ('Loan', 'Loan'),
    ('Others','Others')
    )
class Schemes(models.Model):
    scheme_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.scheme_name

class Supervisor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rep_scheme = models.ForeignKey(Schemes, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Farm(models.Model):
    # User = settings.AUTH_USER_MODEL
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    farm_number = models.CharField(max_length=100, blank=True)
    farm_name = models.CharField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=100, blank=True)
    other_number = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    cultivation_plan = models.CharField(choices = CULTIVATION_CHOICES, default = 'Individual', max_length=100)
    capital = models.CharField(choices = CAPITAL, default = 'Savings', max_length=100)
    scheme = models.ForeignKey(Schemes, on_delete=models.CASCADE)

    def __str__(self):
        return self.farm_name

    

