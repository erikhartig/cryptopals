from set_1.challenge_6 import break_by_key_size
from set_2.challenge_4 import AESOracle, get_block_size, is_aes_in_ecb, RemovePadding


def test_determine_block_size():
    oracle = AESOracle()
    assert 16 == get_block_size(oracle)


def test_is_ecb():
    oracle = AESOracle()
    assert is_aes_in_ecb(oracle, 16)


def test_remove_padding():
    oracle = AESOracle()
    block_size = 16
    wrapped_oracle = RemovePadding(oracle, block_size)
    ciphertext_1 = wrapped_oracle.encrypt_cbc()
    ciphertext_2 = wrapped_oracle.encrypt_cbc()
    assert ciphertext_2[0:32] == ciphertext_1[0:32]


def test_create_dictionary():
    oracle = AESOracle()
    block_size = 16
    base_block = b"A" * (block_size - 1)
    answer = b""

    wrapped_oracle = RemovePadding(oracle, block_size)
    result = wrapped_oracle.encrypt_cbc(base_block)
    expected = result[0:block_size]
    for b in range(10):
        for i in range(0xff):
            value = base_block + i.to_bytes(1, "big")
            ciphertext = wrapped_oracle.encrypt_cbc(value)
            if expected == ciphertext[0:16]:
                answer += i.to_bytes(1, "big")
                base_block = value[1:]
    print(answer)


def _get_data_from_file(name):
    data = ""
    with open(f"/Users/erikhartig/pythonProject/tests/unit_tests/set_2/files/{name}") as f:
        lines = f.readlines()
        for line in lines:
            data += line
    return data
