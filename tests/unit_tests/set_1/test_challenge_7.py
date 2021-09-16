from set_1.challenge_7 import decrypt_aes
from tests.unit_tests.set_1.helper import DECRYPTED_STRING


def test_decrypt():
    key = "YELLOW SUBMARINE"
    crypto_text = _get_data_from_file()
    plaintext = decrypt_aes(crypto_text, key).decode()
    assert DECRYPTED_STRING in plaintext


def _get_data_from_file():
    data = ""
    with open("/Users/erikhartig/pythonProject/tests/unit_tests/set_1/files/challenge_7.txt") as f:
        lines = f.readlines()
        for line in lines:
            data += line
    return data
