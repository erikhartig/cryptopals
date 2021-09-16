from set_1.challenge_8 import check_for_ecb


def test_thing():
    ciphertext_list = _get_data_from_file()
    ecb = check_for_ecb(ciphertext_list)
    assert ecb == "d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5" \
                  "708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd2" \
                  "8397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040d" \
                  "eb0ab51b29933f2c123c58386b06fba186a"


def _get_data_from_file():
    with open("/Users/erikhartig/pythonProject/tests/unit_tests/set_1/files/challenge_8.txt") as f:
        lines = f.readlines()
        return lines
