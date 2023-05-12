def encrypt(text, key):
    encrypted = ''
    for char in text:
        if char.isalpha():
            char_code = ord(char.lower()) - ord('a')
            encrypted += key[char_code]
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted, key):
    decrypted = ''
    for char in encrypted:
        if char.isalpha():
            char_code = key.index(char.lower())
            decrypted += chr(char_code + ord('a'))
        else:
            decrypted += char
    return decrypted

if __name__=='__main__':
    text = 'hello world'
    key = 'kqoxysjmnuzvbtphalfgdcierw'
    encrypted_text = encrypt(text, key)
    print(encrypted_text)
    print(decrypt(encrypted_text, key))