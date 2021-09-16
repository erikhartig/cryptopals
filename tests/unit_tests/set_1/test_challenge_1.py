from set_1.challenge_1 import hex_to_bytes, hex_to_base64


def test_hex_to_bytes():
    assert b"\x01" == hex_to_bytes("1")
    assert b"\x02" == hex_to_bytes("2")
    assert b"\x0a" == hex_to_bytes("a")
    assert b"\x0f" == hex_to_bytes("f")


def test_multiple_hex_to_bytes():
    assert b"\x10" == hex_to_bytes("10")
    assert b"\xaf" == hex_to_bytes("af")
    assert b"\x0a\x10" == hex_to_bytes("a10")
    assert b"\x10\x10" == hex_to_bytes("1010")


def test_whole_problem():
    hex_to_convert = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert expected == hex_to_base64(hex_to_convert)
