from django.shortcuts import render

# Create your views here.

def landing(request):

    name = 'Шерстяная сотона!'
    current_day = "01.01.2017"

    return render(request, 'landing/landing.html', locals())