from set_1.challenge_2 import xor_hex


def test_xor_hex():
    hex_1 = "1c0111001f010100061a024b53535009181c"
    hex_2 = "686974207468652062756c6c277320657965"
    result = "746865206b696420646f6e277420706c6179"
    assert result == xor_hex(hex_1, hex_2)
