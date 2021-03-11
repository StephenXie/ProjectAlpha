from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from citator.forms import CitatorForm
from citator.script import GetResult,GetWordCount
def CitatorView(request):
    return render(request,'citator.html')

def CitatorPost(request):
    try:
        content = request.POST.get('content',0)
        # content = list(map(int, content))
    except:
        return HttpResponse("Integer Value Needed")
    args = {"content": GetResult(content), "count":GetWordCount(content)}
    return render(request,'citator.html',args)
