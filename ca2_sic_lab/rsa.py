# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:36:28 2022

@author: 19pt28
"""

import sympy
import random

min_val = 31
max_val = 2 ** 32


def gcd(a: int, b: int):
    if b == 0:
        return a
    return gcd(b, a % b)


def choose_e(phi_n: int):
    e = 0
    while gcd(phi_n, e) != 1:
        e = random.randint(1, phi_n)
    return e


def e_gcd(a: int, b: int):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = e_gcd(b % a, a)
        return g, x - (b // a) * y, y


def mod_inv(a: int, m: int):
    g, x, y = e_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def generate_keys():
    p, q = sympy.randprime(min_val, max_val), sympy.randprime(min_val, max_val)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = choose_e(phi_n)
    e_1 = mod_inv(e, phi_n)
    d = e_1 % phi_n

    private_key = (d, n)
    public_key = (e, n)

    return private_key, public_key


def encrypt(msg: list[hex], public_key: tuple):
    e, n = public_key
    return [hex(pow(int(char, 16), e, n)) for char in msg]


def decrypt(msg: list[str], priv_key: tuple):
    d, n = priv_key
    return [hex(pow(int(char, 16), d, n)) for char in msg]


if __name__ == "__main__":
    priv_key, public_key = generate_keys()

    print(priv_key, public_key)

    f = open("textfile.txt", "r")
    msg = f.read().encode('utf-8')
    print([i for i in msg])
    new_msg = ['0x' + str(hex(msg[i]).split('0x')[1]) + str(hex(msg[i + 1]).split('0x')[1]) + str(
        hex(msg[i + 2]).split('0x')[1]) + str(hex(msg[i + 3]).split('0x')[1]) for i in
               range(0, len(msg) - (len(msg) % 4), 4)]
    print(new_msg)
    # msg = (''.join(['|' for i in range(len(msg) % 4)])).encode('utf-8')

    enc_msg = encrypt(new_msg, public_key)
    print(enc_msg)
    dec_msg = decrypt(enc_msg, priv_key)
    print(dec_msg)

    final_msg = [msg.split('0x')[1] for msg in dec_msg]
    final_msg = [[int('0x'+line[i:i+2], 16) for i in range(0, len(line), 2)] for line in final_msg]
    print(final_msg)
    final_msg = [chr(char) for character in final_msg for char in character]
    print(''.join(final_msg))
    # final_msg = (''.join(dec_msg)).encode('utf-8')

    # print(final_msg)
