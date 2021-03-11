from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from citator.forms import CitatorForm

def CitatorView(request):
    return render(request,'citator.html')

def CitatorPost(request):
    content = int(request.POST.get('content',0))
    args = {"content": content*7}
    return render(request,'citator.html',args)
