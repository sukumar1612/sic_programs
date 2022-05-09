import hashlib
import hmac
import os

shared_key = os.urandom(32)

if __name__ == "__main__":
    rb = os.urandom(24)

    alice_hash = (hmac.new(rb, shared_key, hashlib.md5).digest(), rb)

    bob_verify = hmac.new(alice_hash[1], shared_key, hashlib.md5).digest()
    print(bob_verify == alice_hash[0])
