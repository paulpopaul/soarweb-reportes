from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404
from .models import IdCard
# Create your views here.


def idcard_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    template = 'idcard/idcard_list.html'
    idcard_list = IdCard.objects.filter(status='Published')
    light = IdCard.objects.filter(theme='Light', status='Published')
    dark = IdCard.objects.filter(theme='Dark')
    blue = IdCard.objects.filter(theme='Blue')
    green = IdCard.objects.filter(theme='Green')
    context = {
        'idcard_list': idcard_list,
        'light': light,
        'dark': dark,
        'blue': blue,
        'green': green,
    }
    return render(request, template, context)


def idcard_detail(request, slug):
    template = 'idcard/idcard_detail.html'
    idcard = get_object_or_404(IdCard, slug=slug)
    context = {
        'idcard': idcard,
    }
    return render(request, template, context)

