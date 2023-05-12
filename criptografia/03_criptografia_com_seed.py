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

if __name__ == '__main__':
    seed = 123446544
    encrypted_text = encrypt('hello world', seed)
    print(encrypted_text)
    print(decrypt(encrypted_text, seed))