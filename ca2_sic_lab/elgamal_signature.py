import random


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    return gcd(b, a % b)


def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)

    return x % c


def key_gen(q: int):
    a = random.randint(pow(2, 16), q)
    while gcd(a, q) != 1:
        a = random.randint(pow(2, 16), q)
    return a


def compute_pre_keys():
    q = random.randint(pow(2, 16), pow(2, 32))
    g = random.randint(2, q)
    a = key_gen(q)

    return q, g, a


def generate_public_private_keys():
    q, g, a = compute_pre_keys()
    f = q
    h = power(g, a, q)

    pub_key = (f, h, q, g)
    priv_key = (a, q)

    return pub_key, priv_key


def encrypt_message(pub_key, message):
    k = key_gen(q=pub_key[2])
    p = power(pub_key[3], k, pub_key[2])
    s = power(pub_key[1], k, pub_key[2])

    return p, message * s


def decrypt_message(priv_key, enc_message):
    ss = power(enc_message[0], priv_key[0], priv_key[1])

    return int(enc_message[1] / ss)


def encrypt_4_bytes(priv_keys):
    f = open("textfile.txt", "r")
    msg = f.read().encode('utf-8')
    print(msg)

    print([i for i in msg])
    new_msg = ['0x' + str(hex(msg[i]).split('0x')[1]) + str(hex(msg[i + 1]).split('0x')[1]) + str(
        hex(msg[i + 2]).split('0x')[1]) + str(hex(msg[i + 3]).split('0x')[1]) for i in
               range(0, len(msg) - (len(msg) % 4), 4)]
    print(new_msg)

    enc_msg = [encrypt_message(priv_keys, int(new_msg[msg], 16)) for msg in range(0, len(new_msg))]

    return enc_msg


def decrypt_4_bytes(message, pub_keys):
    dec_msg = [hex(decrypt_message(pub_keys, msg)) for msg in message]

    print(dec_msg)

    final_msg = [msg.split('0x')[1] for msg in dec_msg]
    final_msg = [[int('0x' + line[i:i + 2], 16) for i in range(0, len(line), 2)] for line in final_msg]
    print(final_msg)
    final_msg = [chr(char) for character in final_msg for char in character]
    return ''.join(final_msg)


if __name__ == "__main__":
    public_keys, private_keys = generate_public_private_keys()
    msg = encrypt_4_bytes(public_keys)
    print(decrypt_4_bytes(msg, private_keys))
