import collections
from functools import partial
from multiprocessing import Pool
from statistics import mode, mean

from set_1.challenge_6 import base64_to_bytes, break_by_key_size
from set_1.challenge_8 import check_repetitions
from set_2.challenge_2.aes import encrypt_aes
from set_2.challenge_3 import generate_aes_key, pad_plaintext


class AESOracle:
    def __init__(self):
        self._key = generate_aes_key()
        base64_plaintext = _get_data_from_file("challenge_4.txt")
        self._static_text = base64_to_bytes(base64_plaintext)

    def encrypt_cbc(self, bytes_to_prepend=b""):
        plaintext = bytes_to_prepend + self._static_text
        plaintext = pad_plaintext(plaintext)
        return encrypt_aes(plaintext, self._key)


def get_block_size(oracle, max_size=150):
    aes_key_sizes = [16, 24, 32]

    with Pool(5) as p:
        results = p.map(partial(_test_length, oracle=oracle), range(max_size))
    counter = collections.Counter(results)

    del counter[max(counter.keys())]
    del counter[min(counter.keys())]
    estimated_value = mean(counter.values())
    return min(aes_key_sizes, key=lambda x: abs(x - estimated_value))


class RemovePadding:
    def __init__(self, oracle, block_size):
        self.oracle = oracle
        self.block_size = block_size
        padding_string = b"B" * block_size
        garbage_char = b"Z"
        ciphertext = self.oracle.encrypt_cbc(padding_string * self.block_size)
        chunks = break_by_key_size(ciphertext, self.block_size)
        results = collections.Counter(chunks)
        padding_check = max(results, key=results.get)

        for extra_padding in range(self.block_size):
            test_string = (garbage_char * extra_padding) + padding_string
            for i in range(self.block_size):
                ciphertext = self.oracle.encrypt_cbc(test_string)
                chunks = break_by_key_size(ciphertext, block_size)
                if padding_check in chunks:
                    self.padding_string = test_string
                    self.padding_check = padding_check
                    return

    def encrypt_cbc(self, bytes_to_prepend=b""):
        while True:
            ciphertext = self.oracle.encrypt_cbc(self.padding_string + bytes_to_prepend)
            chunks = break_by_key_size(ciphertext, self.block_size)
            if self.padding_check in chunks:
                return ciphertext.split(self.padding_check)[1]


def _test_length(length, oracle):
    lengths = []
    text = b"A"*length
    for i in range(10):
        lengths.append(len(oracle.encrypt_cbc(text)))
    return mode(lengths)


def is_aes_in_ecb(oracle, block_size):
    ciphertext = oracle.encrypt_cbc(b"A" * 4 * block_size)
    if check_repetitions(ciphertext) > 1:
        return True
    return False

def _get_data_from_file(name):
    data = ""
    with open(f"/Users/erikhartig/pythonProject/tests/unit_tests/set_2/files/{name}") as f:
        lines = f.readlines()
        for line in lines:
            data += line
    return data
