def caesar_encrypt(plain_text, key):
    encrypted = list(plain_text)
    for i in range(len(encrypted)):
        if encrypted[i].isalpha():
            encrypted[i] = get_letter_val(encrypted[i],key)
    return "".join(encrypted)
def get_letter_val(letter, key):
    if letter.isupper():
        return chr((((ord(letter)-ord("A"))+key)%26)+ord("A"))
    else:
        return chr((((ord(letter)-ord("a"))+key)%26)+ord("a"))
def caesar_decrypt(encrypted, key):
    plain_text = list(encrypted)
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            plain_text[i] = get_letter_val(encrypted[i],-key)
    return "".join(plain_text)