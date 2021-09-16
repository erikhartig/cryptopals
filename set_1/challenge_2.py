from set_1.challenge_1 import hex_to_bytes


def xor_hex(hex_1, hex_2):
    hex_1 = hex_to_bytes(hex_1)
    hex_2 = hex_to_bytes(hex_2)
    result = _xor_hex(hex_1, hex_2)
    return result.hex()


def _xor_hex(hex_1: bytes, hex_2: bytes):
    if len(hex_1) != len(hex_2):
        raise AttributeError("hex_1 and hex_2 have different lengths")
    hex_final = b""
    for i in range(len(hex_1)):
        hex_final += (hex_1[i] ^ hex_2[i]).to_bytes(length=1, byteorder="big")
    return hex_final
