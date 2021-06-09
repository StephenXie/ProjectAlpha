from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from formatter.forms import FormatterForm
from formatter.scripts import GetResult, GetWordCount, GetCharCount


def FormatterView(request):
    if request.path == "/formatter/post":
        return HttpResponseRedirect("/formatter")
    if request.method == "POST":
        try:
            content = request.POST.get('content', 0)
            style = request.POST.get('style_type', "none")
        except:
            return HttpResponse("Integer Value Needed")
        args = {"content": GetResult(content, style), "WordCount": GetWordCount(
            content), "CharCount": GetCharCount(content)}
        return render(request, 'formatter.html', args)
    else:
        return render(request, 'formatter.html')