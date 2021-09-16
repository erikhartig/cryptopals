from set_1.challenge_6 import base64_to_bytes
from set_2.challenge_2.aes import _galois_multiplication
from set_2.challenge_2.cbc import encrypt_cbc, decrypt_cbc


def test_encrypt_cbc_chunk():
    plaintext = b"\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10"
    ciphertext = b"\xff\x0b\x84\x4a\x08\x53\xbf\x7c\x69\x34\xab\x43\x64\x14\x8f\xb9"
    key = b"\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98"
    iv = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    result = encrypt_cbc(plaintext, key, iv)
    assert result == ciphertext


def test_decrypt_cbc_chunk():
    plaintext = b"\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10"
    ciphertext = b"\xff\x0b\x84\x4a\x08\x53\xbf\x7c\x69\x34\xab\x43\x64\x14\x8f\xb9"
    key = b"\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98"
    iv = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    assert plaintext == decrypt_cbc(ciphertext, key, iv)


def test_decrypt_file():
    ciphertext = _get_data_from_file()
    ciphertext = base64_to_bytes(ciphertext)
    iv = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    key = b"YELLOW SUBMARINE"
    result = decrypt_cbc(ciphertext, key, iv)
    print(result.decode())


def test_galois_multiplication():
    assert _galois_multiplication(128, 2).bit_length() <= 8


def _get_data_from_file():
    data = ""
    with open("/Users/erikhartig/pythonProject/tests/unit_tests/set_2/files/challenge_2.txt") as f:
        lines = f.readlines()
        for line in lines:
            data += line
    return data
