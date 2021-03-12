from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
# from citator.forms import CitatorForm
# from citator.script import GetResult,GetWordCount, GetCharCount
from cryptic.script import caesar, vigenere_encrypt, vigenere_decrypt
def CrypticView(request):
    return render(request,'cryptic.html')

def CrypticPost(request):
    try:
        content = request.POST.get('content',0)
        key = int(request.POST.get('key',0)) % 26
        if key<0:
            key = 26-abs(key)
        crypt_type = request.POST.get('type',"encrypt")
        # content = list(map(int, content))
    except:
        return HttpResponse("Error")
    if crypt_type=="encrypt":
        val = caesar(content,key)
    elif crypt_type=="decrypt":
        val = caesar(content,-key)
    args = {"content": val}
    return render(request,'cryptic.html',args)
