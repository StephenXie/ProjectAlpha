from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
# from citator.forms import CitatorForm
# from citator.script import GetResult,GetWordCount, GetCharCount
from cryptic.script import caesar, vigenere_encrypt, vigenere_decrypt
def CrypticView(request):
    return render(request,'cryptic.html')

def CrypticPost(request):
    content = request.POST.get('content',0)
    cipher_type = request.POST.get("cipher_type")
    crypt_type = request.POST.get('method_type',"encrypt")
    if cipher_type == "caesar":
        try:
            key = int(request.POST.get('caesar_key',0)) % 26
        except:
            return HttpResponse("Error")
        if key<0:
            key = 26-abs(key)
        if crypt_type=="encrypt":
            val = caesar(content,key)
        elif crypt_type=="decrypt":
            val = caesar(content,-key)

    elif cipher_type == "vigenere":
        key = request.POST.get('vigenere_key')
        content = content.lower()
        if crypt_type == "encrypt":
            val = vigenere_encrypt(content,key)
        elif crypt_type == "decrypt":
            val = vigenere_decrypt(content,key)

    args = {"content": val}
    return render(request,'cryptic.html',args)
