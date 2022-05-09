from des import DesKey
import os

shared_key = DesKey(os.urandom(24))

if __name__ == "__main__":
    rb = os.urandom(24)

    # challenge
    alice_encrypt = shared_key.encrypt(rb, padding=True)

    # response
    bob_verify = shared_key.decrypt(alice_encrypt, padding=True) == rb
    print(bob_verify)