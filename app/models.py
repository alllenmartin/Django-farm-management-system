from django.db import models
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farm_number = models.CharField(max_length=100, blank=True)
    farm_name = models.CharField(max_length=100, blank=True)
    scheme = models.ForeignKey(Schemes, on_delete=models.CASCADE)

    def __str__(self):
        return self.farm_name
