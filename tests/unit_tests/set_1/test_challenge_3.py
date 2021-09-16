
from set_1.challenge_3 import decode_hex


def test_decode():
    hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    decoded_string = decode_hex(hex_string).decoded_text
    assert decoded_string == "Cooking MC's like a pound of bacon"
