import codecs


def hex_to_bytes(hex_to_convert):
    if len(hex_to_convert) % 2 == 1:
        hex_to_convert = "0" + hex_to_convert
    return bytes.fromhex(hex_to_convert)


def bytes_to_base64(bytes_to_convert: bytes):
    return codecs.encode(bytes_to_convert, 'base64')


def hex_to_base64(hex_to_convert):
    raw_bytes = hex_to_bytes(hex_to_convert)
    return bytes_to_base64(raw_bytes).decode().strip()
