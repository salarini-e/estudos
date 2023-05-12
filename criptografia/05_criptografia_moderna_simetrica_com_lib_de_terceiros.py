from cryptography.fernet import Fernet

key = Fernet.generate_key()

message = b'Hello world!'
cipher = Fernet(key)
encrypted_message = cipher.encrypt(message)

decrypted_message = cipher.decrypt(encrypted_message)

print(f'Chave de criptografia: {key}')
print(f'Mensagem criptografada: {encrypted_message}')
print(f'Mensagem descriptografada: {decrypted_message}')
