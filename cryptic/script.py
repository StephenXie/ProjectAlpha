import math
def caesar(text, key):
    res = list(text)
    for i in range(len(res)):
        if res[i].isalpha():
            res[i] = caesar_modify(res[i],key)
    return "".join(res)

def caesar_modify(letter, key):
    if letter.isupper():
        return chr((((ord(letter)-ord("A"))+key)%26)+ord("A"))
    return chr((((ord(letter)-ord("a"))+key)%26)+ord("a"))

def caesar_brute(text):
    res = []
    for i in range(26):
        res.append(str(i)+". "+caesar(text,-i))
    return "\n".join(res)

def vigenere_encrypt(text, keyword):
    res = list(text)
    j = 0
    for i in range(len(res)):
        if res[i].isalpha():
            val = ((ord(res[i]) - ord("a")) + (ord(keyword[j%len(keyword)]) - ord("a")))%26
            res[i] = chr(val+ord("a"))
            j+=1
    return "".join(res)

def vigenere_decrypt(text, keyword):
    res = list(text)
    j = 0
    for i in range(len(res)):
        if res[i].isalpha():
            val = (26 + (ord(res[i]) - ord("a")) - (ord(keyword[j%len(keyword)]) - ord("a")))%26
            res[i] = chr(val+ord("a"))
            j+=1
    return "".join(res)

def affine_encrypt(text, a, b):
    text = list(text)
    for i in range(len(text)):
        if text[i].isalpha():
            val = ord(text[i])-ord("a")
            val = a*val + b
            val %= 26
            text[i] = chr(val + ord("a"))
    return "".join(text)

def affine_decrypt(text,a,b):
    text = list(text)
    a_inv = 0
    while (a*a_inv)%26 != 1:
        a_inv+=1
    for i in range(len(text)):
        if text[i].isalpha():
            val = ord(text[i])-ord("a")
            val = (val - b) * a_inv
            val %= 26
            text[i] = chr(val + ord("a"))
    return "".join(text)