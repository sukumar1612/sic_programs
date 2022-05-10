import math
import os

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


if __name__ == "__main__":
    pa, pra = generate_keys()
    pb, prb = generate_keys()

    ra = str(os.urandom(16)).encode('utf-8')
    rb = str(os.urandom(16)).encode('utf-8')
    print(ra)
    print(rb)
    bob = enc_4_bytes(ra, pb)
    bob_de = dec_4_bytes(bob, prb)

    alice = (enc_4_bytes(ra, pa), enc_4_bytes(rb, pa))
    alice_de = (dec_4_bytes(alice[0], pra), dec_4_bytes(alice[1], pra))

    print(alice_de[0] == ra.decode('utf-8'))
    print(alice_de[1] == rb.decode('utf-8'))
