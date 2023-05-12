import random

def encrypt(text, seed):
    random.seed(seed)
    key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=len(text)))
    encrypted = ''
    for i in range(len(text)):
        char = text[i]
        key_char = key[i]
        encrypted += chr(ord(char) ^ ord(key_char))
    return encrypted

def decrypt(encrypted, seed):
    random.seed(seed)
    key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=len(encrypted)))
    decrypted = ''
    for i in range(len(encrypted)):
        char = encrypted[i]
        key_char = key[i]
        decrypted += chr(ord(char) ^ ord(key_char))
    return decrypted

import time

def measure_time(text, encrypted_text):
    return 'preguiça de fazer isso agora'

if __name__ == '__main__':
    seed = 1234
    text='hello world'
    encrypted_text = encrypt(text, seed)
    print(encrypted_text)
    print(decrypt(encrypted_text, seed))
    measure_time(text, encrypted_text)
    