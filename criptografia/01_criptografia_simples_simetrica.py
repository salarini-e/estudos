import random

def encrypt(texto, key):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for letra in texto.lower():
        if letra in alfabeto:
            letra_index = alfabeto.index(letra)
            encrypted += key[letra_index]
        else:
            encrypted += letra
    return encrypted

if __name__ == '__main__':
    texto=input('Entre com o texto a ser criptografado:\n >>')
    key='qwertyuiopasdfghjklzxcvbnm'
    # key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=16))
    encrypted_text = encrypt(texto, key)
    print('texto criptografado: ', encrypted_text)    