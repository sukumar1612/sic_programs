import sympy

min_v = 2 ** 9
max_v = 2 ** 16


def find_generator(p):
    for i in range(2, p):
        lst = set()
        for j in range(1, p):
            lst.add(pow(i, j, p))

        if len(lst) == p - 1:
            return i


def generate_keys():
    p = sympy.randprime(min_v, max_v)
    d = sympy.randprime(1, p - 2)
    e1 = find_generator(p)
    e2 = pow(e1, d, p)

    public_key = (e1, e2, p)
    private_key = (d, p)

    return public_key, private_key


def encryption(public_key, msg):
    r = sympy.randprime(1, public_key[2] - 1)
    c1 = pow(public_key[0], r, public_key[2])
    c2 = pow(msg, 1, public_key[2]) * pow(public_key[1], r, public_key[2]) % public_key[2]

    enc_message = (c1, c2)
    return enc_message


def decryption(private_key, enc_msg):
    c1d_1 = pow(pow(enc_msg[0], private_key[0], private_key[1]), -1, private_key[1])
    dec_message = enc_msg[1] * c1d_1 % private_key[1]

    return dec_message


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
    public_key, private_key = generate_keys()

    f = open("textfile.txt", 'r')
    message = f.read().encode('utf-8')
    enc = [encryption(public_key, i) for i in message]
    print(enc)
    dec = ''.join([chr(decryption(private_key, i)) for i in enc])
    print(dec)
