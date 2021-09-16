from set_2.challenge_1 import pad_pkcs7_string


def test_pkcs7_padding():
    sample_text = "YELLOW SUBMARINE"
    padded_text = pad_pkcs7_string(sample_text, 20)
    assert padded_text == b"YELLOW SUBMARINE\x04\x04\x04\x04"


def test_pkcs7_padding_not_needed():
    sample_text = "YELLOW SUBMARINE"
    padded_text = pad_pkcs7_string(sample_text, 16)
    assert padded_text == b"YELLOW SUBMARINE"
