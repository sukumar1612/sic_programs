import math
import hashlib
import hmac
import sympy

min_val = 2 ** 8
max_val = 2 ** 128


def generate_primes():
    p = 0
    q = 0
    while p == q:
        p = sympy.randprime(min_val, max_val)
        q = sympy.randprime(min_val, max_val)

    return p, q


def gen_co_primes(a, b, phi_n):
    e = sympy.randprime(a, b)
    while math.gcd(e, phi_n) != 1:
        e = sympy.randprime(a, b)

    return e


def generate_keys():
    p, q = generate_primes()
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = gen_co_primes(a=min_val, b=phi_n, phi_n=phi_n)

    d = pow(e, -1, phi_n)
    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


def encryption(public_key, msg):
    return pow(msg, public_key[0], public_key[1])


def decryption(private_key, enc_msg):
    return pow(enc_msg, private_key[0], private_key[1])


def enc_4_bytes(message, public_key):
    message = [hex(msg).split('0x')[1] for msg in message]
    new_message = [message[i] + message[i + 1] + message[i + 2] + message[i + 3] for i in
                   range(0, len(message) - len(message) % 4, 4)]
    last_bit = ''.join([message[i] for i in range(len(message) - len(message) % 4, len(message))])
    if len(last_bit) != 0:
        new_message.append(last_bit)

    print(new_message)
    new_message = [int('0x' + new_message[i], 16) for i in range(0, len(new_message))]
    new_message = [encryption(public_key=public_key, msg=new_message[i]) for i in range(0, len(new_message))]

    return new_message


def dec_4_bytes(enc_message, private_key):
    dec_message = [hex(decryption(private_key=private_key, enc_msg=enc_message[i])) for i in range(0, len(enc_message))]
    dec_message = [dec_message[i].split('0x')[1] for i in range(0, len(dec_message))]
    dec_message = [[msg[i:i + 2] for i in range(0, len(msg), 2)] for msg in dec_message]
    dec_message = ''.join([chr(int('0x' + i, 16)) for msg in dec_message for i in msg])

    return dec_message


def sign_document(private_key, file_name):
    f = open(file_name, 'r')
    message = f.read().encode('utf-8')
    digest = hmac.HMAC(key=b'', msg=message, digestmod=hashlib.md5).digest()
    digest = str(digest).encode('utf-8')
    return message, enc_4_bytes(message=digest, public_key=private_key)


def verify_document(public_key, signature):
    message = signature[0]
    digest = hmac.HMAC(key=b'', msg=message, digestmod=hashlib.md5).digest()
    vdigest = dec_4_bytes(signature[1], public_key)
    print(digest)
    print(vdigest)
    return str(digest) == str(vdigest)


if __name__ == "__main__":
    p, q = generate_keys()

    signature = sign_document(p, 'textfile.txt')
    print(signature)
    print(verify_document(q, signature))
