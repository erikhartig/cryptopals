from set_1.challenge_8 import check_repetitions
from set_2.challenge_3 import random_encrypt_text, is_aes_in_ecb


def test_detect_aes_method():
    plaintext = _get_data_from_file("challenge_3.txt").encode()
    ciphertexts = _generate_ciphertexts(plaintext)
    _check_success_rate(ciphertexts)


def test_detect_aes_method_medium():
    plaintext = _get_data_from_file("challenge_3_medium.txt").encode()
    ciphertexts = _generate_ciphertexts(plaintext)
    _check_success_rate(ciphertexts)


def test_detect_aes_method_easy():
    plaintext = _get_data_from_file("challenge_3_easy.txt").encode()
    ciphertexts = _generate_ciphertexts(plaintext)
    _check_success_rate(ciphertexts)


def _generate_ciphertexts(plaintext):
    if check_repetitions(plaintext) == 0:
        print("Warning this text won't be detectable because it contains no duplicated 16 byte chunks of plaintext")
    ciphertexts = []
    for i in range(100):
        ciphertexts.append(random_encrypt_text(plaintext))
    return ciphertexts


def _check_success_rate(ciphertexts):
    failures = 0
    for ciphertext in ciphertexts:
        if is_aes_in_ecb(ciphertext[1]):
            print(f"I think this is ecb and it is {ciphertext[0]}")
            if ciphertext[0] != "ecb":
                failures += 1
        elif ciphertext[0] == "ecb":
            failures += 1
            print("failed to detect aes but was ecb")
    print(f"failed on {failures} out of 100")


def _get_data_from_file(name):
    data = ""
    with open(f"/Users/erikhartig/pythonProject/tests/unit_tests/set_2/files/{name}") as f:
        lines = f.readlines()
        for line in lines:
            data += line
    return data
