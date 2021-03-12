def caesar(text, key):
    res = list(text)
    for i in range(len(res)):
        if res[i].isalpha():
            res[i] = ceasar_modify(res[i],key)
    return "".join(res)

def ceasar_modify(letter, key):
    if letter.isupper():
        return chr((((ord(letter)-ord("A"))+key)%26)+ord("A"))
    else:
        return chr((((ord(letter)-ord("a"))+key)%26)+ord("a"))

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
            print(res)
            val = (26 + (ord(res[i]) - ord("a")) - (ord(keyword[j%len(keyword)]) - ord("a")))%26
            res[i] = chr(val+ord("a"))
            j+=1
    return "".join(res)