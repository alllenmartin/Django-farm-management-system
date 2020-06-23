from django.contrib import admin
from . models import Schemes
from .models import Farm
from .models import Supervisor

admin.site.register(Schemes)
admin.site.register(Farm)
admin.site.register(Supervisor)