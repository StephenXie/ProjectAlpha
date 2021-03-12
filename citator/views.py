from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from citator.forms import CitatorForm
from citator.script import GetResult,GetWordCount, GetCharCount
def CitatorView(request):
    return render(request,'citator.html')

def CitatorPost(request):
    try:
        content = request.POST.get('content',0)
        style = request.POST.get('style_type',"none")
    except:
        return HttpResponse("Integer Value Needed")
    args = {"content": GetResult(content,style), "WordCount":GetWordCount(content), "CharCount":GetCharCount(content)}
    return render(request,'citator.html',args)
