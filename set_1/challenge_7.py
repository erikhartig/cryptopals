import Crypto.Cipher.AES

from set_1.challenge_6 import base64_to_bytes


def decrypt_aes(ciphertext, key):
    key = bytes(key, "ascii")
    cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_ECB)
    ciphertext = base64_to_bytes(ciphertext)
    return cipher.decrypt(ciphertext)
