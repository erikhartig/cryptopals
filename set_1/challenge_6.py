import base64
import math

from set_1.challenge_3 import decode_single_character_xor
from set_1.challenge_5 import rotating_character_xor


def decrypt_repeating_xor(ciphertext):
    key_size = get_key_size(ciphertext)
    key = decrypt_using_key_size(ciphertext, key_size)
    decrypted_string = rotating_character_xor(ciphertext, key)
    return decrypted_string


def get_key_size(ciphertext):
    distances = []
    number_of_blocks = 4
    for key_size in range(2, min(41, math.floor(len(ciphertext)/(2 * (number_of_blocks + 1))))):
        distance = 0
        for i in range(0, number_of_blocks):
            first_block = ciphertext[key_size * i * 2:key_size * (i + 1) * 2]
            second_block = ciphertext[key_size * (i + 1) * 2:key_size * (i + 2) * 2]
            distance += hamming_distance(first_block, second_block)
        adjusted_distance = distance / key_size
        distances.append((key_size, adjusted_distance))
    distances.sort(key=lambda x: x[1])
    return distances[0][0]


def break_by_key_size(ciphertext: bytes, key_size: int):
    i = 0
    chunks = []
    while (i + 1) * key_size < len(ciphertext):
        chunks.append(ciphertext[i*key_size: (i + 1)*key_size])
        i += 1
    if i * key_size < len(ciphertext):
        chunks.append(ciphertext[i*key_size:])
    return chunks


def decrypt_using_key_size(ciphertext, key_size):
    chunks = break_by_key_size(ciphertext, key_size)
    final_key = b""
    for i in range(0, key_size):
        transposed_chunk = bytes([chunk[i] for chunk in chunks if i < len(chunk)])
        decoded_string = decode_single_character_xor(transposed_chunk)
        final_key += bytes([decoded_string.key])
    return final_key


def hamming_distance(first_string: bytes, second_string: bytes):
    difference = 0
    for i in range(len(first_string)):
        xor = first_string[i] ^ second_string[i]
        difference += int(xor).bit_count()
    return difference


def base64_to_bytes(base64_str: str) -> bytes:
    return base64.b64decode(base64_str.encode('ascii'))
