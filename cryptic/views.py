from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
# from citator.forms import CitatorForm
# from citator.script import GetResult,GetWordCount, GetCharCount
from cryptic.script import caesar_decrypt,caesar_encrypt
def CrypticView(request):
    return render(request,'cryptic.html')

def CrypticPost(request):
    try:
        content = request.POST.get('content',0)
        key = abs(int(request.POST.get('key',0)))
        crypt_type = request.POST.get('type',"encrypt")
        # content = list(map(int, content))
    except:
        return HttpResponse("Error")
    if crypt_type=="encrypt":
        val = caesar_encrypt(content,key)
    elif crypt_type=="decrypt":
        val = caesar_decrypt(content,key)
    args = {"content": val}
    return render(request,'cryptic.html',args)
