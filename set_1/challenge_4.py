from set_1.challenge_3 import decode_hex


def find_encoded_hex(lines):
    decoded_strings = []
    for line in lines:
        try:
            decoded_strings.append(decode_hex(line))
        except ValueError:
            pass
    decoded_strings.sort(reverse=True)
    return decoded_strings[0]
