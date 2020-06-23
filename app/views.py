from django.shortcuts import render
from . forms import FarmForm


def farm_form(request):
    form = FarmForm()
    return render(request, 'farm.html', {'form': form})


