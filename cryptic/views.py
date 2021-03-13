from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
# from citator.forms import CitatorForm
# from citator.script import GetResult,GetWordCount, GetCharCount
from cryptic.script import caesar, caesar_brute, vigenere_encrypt, vigenere_decrypt, affine_encrypt, affine_decrypt
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
        elif crypt_type=="brute_force_decrypt":
            val = caesar_brute(content)
    elif cipher_type == "vigenere":
        key = request.POST.get('vigenere_key')
        content = content.lower()
        if crypt_type == "encrypt":
            val = vigenere_encrypt(content,key)
        elif crypt_type == "decrypt":
            val = vigenere_decrypt(content,key)
    elif cipher_type == "affine":
        try:
            a = int(request.POST.get('affine_a',0))
            b = int(request.POST.get('affine_b',0))
        except ValueError:
            return HttpResponse("Error")
        if a!=0 and 26/a == 26//a:
            return HttpResponse("A need to be coprime with 26 or else the substitution will not be unique.")
        content = content.lower()
        if crypt_type == "encrypt":
            val = affine_encrypt(content,a,b)
        elif crypt_type == "decrypt":
            val = affine_decrypt(content,a,b)

    args = {"content": val}
    return render(request,'cryptic.html',args)
