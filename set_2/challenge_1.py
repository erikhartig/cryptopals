def pad_pkcs7(plaintext: bytes, pad: int) -> bytes:
    return plaintext + b"\x04" * (pad - len(plaintext))


def pad_pkcs7_string(plaintext, pad):
    plaintext_bytes = bytes(plaintext, "ascii")
    return pad_pkcs7(plaintext_bytes, pad)
