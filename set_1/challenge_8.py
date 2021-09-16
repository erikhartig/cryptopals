from set_1.challenge_1 import hex_to_bytes
from set_1.challenge_6 import break_by_key_size


def check_repetitions(ciphertext: bytes):
    chunks = break_by_key_size(ciphertext, 16)
    set_chunks = set(chunks)
    return len(chunks) - len(set_chunks)


def check_for_ecb(ciphertext_list):
    highest_val = 0
    highest_ciphertext = ""
    for ciphertext in ciphertext_list:
        ciphertext = ciphertext.strip()
        ciphertext_bytes = hex_to_bytes(ciphertext)
        val = check_repetitions(ciphertext_bytes)
        if val > highest_val:
            highest_val = val
            highest_ciphertext = ciphertext
    return highest_ciphertext
