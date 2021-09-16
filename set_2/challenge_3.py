import random
import secrets

from set_1.challenge_8 import check_repetitions
from set_2.challenge_2.aes import encrypt_aes
from set_2.challenge_2.cbc import encrypt_cbc


def generate_aes_key():
    return secrets.token_bytes(16)


def pad_plaintext(plaintext):
    return secrets.token_bytes(random.randint(5, 10)) + plaintext + secrets.token_bytes(random.randint(5, 10))


def random_encrypt_text(plaintext):
    key = generate_aes_key()
    plaintext = pad_plaintext(plaintext)
    encryption_method = random.randint(0, 1)
    if encryption_method == 0:
        return "ecb", encrypt_aes(plaintext, key)
    else:
        return "cbc", encrypt_cbc(plaintext, key, generate_aes_key())


def is_aes_in_ecb(ciphertext):
    if check_repetitions(ciphertext) > 1:
        return True
    return False
