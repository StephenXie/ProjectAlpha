def caesar_encrypt(plain_text, key):
    encrypted = list(plain_text)
    for i in range(len(encrypted)):
        if encrypted[i].isalpha():
            cur_val = ord(encrypted[i])
            encrypted[i] = chr((((cur_val-ord("a"))+key)%26)+ord("a"))
    return "".join(encrypted)
def caesar_decrypt(encrypted, key):
    plain_text = list(encrypted)
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            cur_val = ord(encrypted[i])
            plain_text[i] = chr((((cur_val-ord("a"))-key)%26)+ord("a"))
    return "".join(plain_text)