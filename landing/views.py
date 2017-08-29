from django.shortcuts import render
from .forms import ProfileForm
from django.db import models

# Create your views here.

def landing(request):

    name = 'Шерстяная сотона!'
    #current_day = models.DateField(auto_now=True) не работает хз почему
    current_day = '01.01.2017'
    form = ProfileForm(request.POST or None)

    return render(request, 'landing/landing.html', locals())