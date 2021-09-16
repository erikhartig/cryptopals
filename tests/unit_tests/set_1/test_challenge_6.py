from set_1.challenge_1 import hex_to_bytes
from set_1.challenge_3 import decode_single_character_xor
from set_1.challenge_5 import decrypt_xor_repeating
from set_1.challenge_6 import hamming_distance, decrypt_repeating_xor,  break_by_key_size, \
    decrypt_using_key_size, base64_to_bytes
from tests.unit_tests.set_1.helper import DECRYPTED_STRING


def test_hamming_distance():
    first_string = "this is a test"
    second_string = "wokka wokka!!!"
    first_string = bytes(first_string, "ascii")
    second_string = bytes(second_string, "ascii")
    dist = hamming_distance(first_string, second_string)
    assert 37 == dist


def test_break_by_key_size():
    ciphertext = "0b3637272a2b2e63622c2e69692a"
    ciphertext = hex_to_bytes(ciphertext)
    chunks = break_by_key_size(ciphertext, 3)
    assert chunks == [b"\x0b\x36\x37", b"\x27\x2a\x2b", b"\x2e\x63\x62", b"\x2c\x2e\x69", b"\x69\x2a"]


def test_break_xor():
    ciphertext = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a" \
                 "3124333a653e2b2027630c692b20283165286326302e27282f"
    ciphertext_bytes = hex_to_bytes(ciphertext)
    key = decrypt_using_key_size(ciphertext_bytes, 3)
    decrypted_string = decrypt_xor_repeating(ciphertext, key.decode())
    assert key == b"ICE"
    assert decrypted_string == "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"


def test_decrypt_chunk():
    ciphertext = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a" \
                 "3124333a653e2b2027630c692b20283165286326302e27282f"
    chunk = ""
    for i in range(len(ciphertext)):
        if i % 6 == 0:
            chunk += ciphertext[i] + ciphertext[i + 1]
    chunk = hex_to_bytes(chunk)
    decoded_string = decode_single_character_xor(chunk)
    assert decoded_string.key.to_bytes(1, "big") == b"I"


def _get_data_from_file():
    data = ""
    with open("/Users/erikhartig/pythonProject/tests/unit_tests/set_1/files/challenge_6.txt") as f:
        lines = f.readlines()
        for line in lines:
            data += line
    return data


def test_base64_to_bytes():
    expected_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    base64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert expected_hex == base64_to_bytes(base64).hex()


def test_decrypt_base64():
    ciphertext = _get_data_from_file()
    ciphertext = base64_to_bytes(ciphertext)
    decrypted_string = decrypt_repeating_xor(ciphertext).decode().strip()

    assert decrypted_string == DECRYPTED_STRING

    print(decrypted_string)
