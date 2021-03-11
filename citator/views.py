from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from citator.forms import CitatorForm
from citator.script import GetResult
def CitatorView(request):
    return render(request,'citator.html')

def CitatorPost(request):
    try:
        content = int(request.POST.get('content',0))
    except ValueError:
        return HttpResponse("Integer Value Needed")
    args = {"content": GetResult(content)}
    return render(request,'citator.html',args)
