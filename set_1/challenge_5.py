from set_1.challenge_1 import hex_to_bytes


def encrypt_xor_repeating(plaintext, key):
    key = bytes(key, "ascii")
    plaintext = bytes(plaintext, "ascii")
    result = rotating_character_xor(plaintext, key)
    return result.hex().strip()


def decrypt_xor_repeating(plaintext, key):
    key = bytes(key, "ascii")
    plaintext = hex_to_bytes(plaintext)
    result = rotating_character_xor(plaintext, key)
    return result.decode("ascii")


def rotating_character_xor(plaintext, key):
    ciphertext = b""
    for i in range(len(plaintext)):
        byte_to_xor = plaintext[i]
        key_byte = key[i % len(key)]
        ciphertext += (byte_to_xor ^ key_byte).to_bytes(length=1, byteorder="big")
    return ciphertext
