from multiprocessing import Pool

from set_2.challenge_2.aes import decrypt_aes, encrypt_aes_chunk
from set_2.challenge_1 import pad_pkcs7


def encrypt_cbc(plaintext, key, initialization_vector):
    ciphertext = b""
    for i in range(0, len(plaintext), 16):
        plaintext_chunk = plaintext[i:i+16]
        plaintext_chunk = pad_pkcs7(plaintext_chunk, 16)
        if i == 0:
            plaintext_chunk = int.from_bytes(plaintext_chunk, "big") ^ int.from_bytes(initialization_vector, "big")
        else:
            plaintext_chunk = int.from_bytes(plaintext_chunk, "big") ^ int.from_bytes(ciphertext[i-16:i], "big")
        ciphertext += encrypt_aes_chunk(plaintext_chunk.to_bytes(16, "big"), key)
    return ciphertext


def decrypt_cbc(ciphertext: bytes, key: bytes, initialization_vector: bytes):
    chunks = []
    for i in range(len(ciphertext), 0, -16):
        if i == 16:
            chunks.append((ciphertext[i-16:i], key, initialization_vector))
        else:
            chunks.append((ciphertext[i-16:i], key, ciphertext[i-32:i-16]))

    with Pool(5) as p:
        results = p.map(_decrypt_cbc_chunk, chunks)
    results.reverse()
    plaintext = b"".join(results)
    plaintext = _remove_pkcs_padding(plaintext)
    return plaintext


def _decrypt_cbc_chunk(args):
    ciphertext = args[0]
    key = args[1]
    initialization_vector = args[2]
    plaintext_chunk = decrypt_aes(ciphertext, key)
    plaintext_chunk = int.from_bytes(plaintext_chunk, "big") ^ int.from_bytes(initialization_vector, "big")
    return plaintext_chunk.to_bytes(16, "big")


def _remove_pkcs_padding(plaintext: bytes):
    while plaintext[-1:] == b"\x04":
        plaintext = plaintext[0:-1]
    return plaintext
