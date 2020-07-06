from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . forms import FarmForm
from . models import Farm
from django.contrib.auth.models import User
from django.contrib import messages

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


@login_required
def registered_users(request):
    users = User.objects.all()
    context = {
    'users': users
    }
    return render(request,'users.html', context)

@login_required()
def user_deactivate(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()
    messages.success(request, "User account has been successfully deactivated!")
    return redirect('app:users')

@login_required()
def user_activate(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = True
    user.save()
    messages.success(request, "User account has been successfully activated!")
    return redirect('app:users')




































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