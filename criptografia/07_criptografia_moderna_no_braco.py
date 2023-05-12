import random
import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def generate_prime_number():
    # Gera um número primo aleatório entre 100 e 999
    while True:
        n = random.randint(100, 999)
        is_prime = True
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            return n

def generate_keys():
    # Gera um par de chaves RSA
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi_n = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi_n-1)
        if gcd(e, phi_n) == 1:
            break

    d = 0
    k = 1
    while True:
        d = (phi_n * k + 1) // e
        if d * e == phi_n * k + 1:
            break
        k += 1

    public_key = (n, e)
    private_key = (n, d)

    return (public_key, private_key)

def encrypt(message, public_key):
    # Criptografa a mensagem usando a chave pública
    n, e = public_key
    encrypted_message = [pow(ord(c), e, n) for c in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    # Descriptografa a mensagem usando a chave privada
    n, d = private_key
    decrypted_message = [chr(pow(c, d, n)) for c in encrypted_message]
    return ''.join(decrypted_message)

# Gera as chaves
public_key, private_key = generate_keys()

# Exemplo de uso
message = 'Hello, world!'
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

print(f'Mensagem original: {message}')
print(f'Mensagem criptografada: {encrypted_message}')
print(f'Mensagem descriptografada: {decrypted_message}')
