from set_1.challenge_5 import encrypt_xor_repeating, decrypt_xor_repeating


def test_encrypt_xor():
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    ciphertext = encrypt_xor_repeating(plaintext, key)
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a31" \
               "24333a653e2b2027630c692b20283165286326302e27282f"
    assert ciphertext == expected


def test_decrypt_xor_basic():
    plaintext = "b"
    key = "I"
    ciphertext = encrypt_xor_repeating(plaintext, key)
    decrypted_text = decrypt_xor_repeating(ciphertext, key)
    assert plaintext == decrypted_text


def test_decrypt_xor():
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    ciphertext = encrypt_xor_repeating(plaintext, key)
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a31" \
               "24333a653e2b2027630c692b20283165286326302e27282f"
    assert ciphertext == expected
    decrypted_text = decrypt_xor_repeating(ciphertext, key)
    assert plaintext == decrypted_text
