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
    return

def vigenere_decrypt(text, keyword):
    return