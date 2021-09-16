from set_1.challenge_4 import find_encoded_hex


def _get_hex_from_files():
    hex_list = []
    with open("/Users/erikhartig/pythonProject/tests/unit_tests/set_1/files/challenge_4.txt") as f:
        lines = f.readlines()
        for line in lines:
            hex_list.append(line.strip())
    return hex_list


def test_strings():
    decoded_string = find_encoded_hex(_get_hex_from_files())
    assert decoded_string.decoded_text == "Now that the party is jumping"
