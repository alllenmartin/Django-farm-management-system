from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . forms import FarmForm
from . models import Farm

@login_required
def farm_form(request):

    allfarms = Farm.objects.all()
    form= FarmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        newfarm = form.save(commit=False)
        newfarm.user = request.user
        newfarm.save()
        return redirect('profile')

    return render(request, 'farm.html', {'form':form})





































# from django.shortcuts import render,redirect
# from . forms import FarmForm
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from authentication. models import Profile

# @login_required
# def farm_form(request):
#     if request.method == "GET":
#         form = FarmForm()
#         return render(request, 'farm.html', {'form': form})
#     else:
#         form=FarmForm(request.POST)
#         if form.is_valid():
#             form=Profile.objects.filter(pk=request.user.pk).first()
#             form.save()
            
#         return redirect('index')


# # def farm_form(request):
# #     if request.method == "POST":
# #         form = FarmForm(request.POST)
# #         if form.is_valid():
# #             form=Profile.objects.filter(pk=request.user.pk).first()
# #             form.save()
# #     else:
# #         form=FarmForm()
# #     return render(request,'farm.html', {'form':form})        

# #        