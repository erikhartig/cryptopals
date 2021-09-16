import math

from set_1.challenge_1 import hex_to_bytes

ENGLISH_FREQUENCY = {
        "a": .08167,
        "b": .01492,
        "c": .02782,
        "d": .04253,
        "e": .12702,
        "f": .02228,
        "g": .02015,
        "h": .06094,
        "i": .06966,
        "j": .00153,
        "k": .00772,
        "l": .04025,
        "m": .02406,
        "n": .06749,
        "o": .07507,
        "p": .01929,
        "q": .00095,
        "r": .05987,
        "s": .06327,
        "t": .09056,
        "u": .02758,
        "v": .00978,
        "w": .02360,
        "x": .00150,
        "y": .01974,
        "z": .00074,
    }


def _single_character_xor(ciphertext: bytes, char):
    hex_final = b""
    for i in range(len(ciphertext)):
        hex_final += (ciphertext[i] ^ char).to_bytes(length=1, byteorder="big")
    return hex_final


def xor_ciphertext(ciphertext: bytes, hex_char):
    try:
        decoded_hex = _single_character_xor(ciphertext, hex_char)
        decoded_string = decoded_hex.decode("ascii")
        return decoded_string
    except UnicodeDecodeError:
        return ""


def decode_hex(ciphertext: str):
    return decode_single_character_xor(hex_to_bytes(ciphertext))


def decode_single_character_xor(ciphertext: bytes):
    decoded_texts = []
    for hex_char in range(256):
        if hex_char == 73:
            pass
        decoded_text = xor_ciphertext(ciphertext, hex_char)
        if decoded_text:
            decoded_texts.append(DecodedText(hex_char, decoded_text))
    decoded_texts.sort(reverse=True)
    if decoded_texts:
        return decoded_texts[0]
    else:
        raise ValueError("No valid decode found")


class DecodedText:
    def __init__(self, key, decoded_text):
        self.key = key
        self.decoded_text = decoded_text.strip()
        self.score = 1
        self._score_text()

    def _score_text(self):
        total_characters = 0
        non_spaces = 0
        spaces = 0
        character_occurrences = {
            "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
            "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,
        }

        for char in self.decoded_text:
            lower_case = char.lower()
            if char in character_occurrences:
                character_occurrences[lower_case] += 1
                total_characters += 1
            elif char == " ":
                spaces += 1
            else:
                non_spaces += 1
        if not total_characters:
            self.score = 0
            return

        # account for letter distribution
        for letter, num_of_occurrences in character_occurrences.items():
            if num_of_occurrences:
                percent = num_of_occurrences/total_characters
                self.score += ENGLISH_FREQUENCY[letter] * _normal_distribution(percent, ENGLISH_FREQUENCY[letter],
                                                                               ENGLISH_FREQUENCY[letter]/4)

        # account for number of non-space non-letter characters
        self.score = self.score * ((len(self.decoded_text)-non_spaces)/len(self.decoded_text)) ** 2

        # account for number of spaces
        self.score = self.score * _normal_distribution(spaces/len(self.decoded_text), .2, .05)

    def __gt__(self, other):
        return self.score > other.score


def _normal_distribution(val, mean, sd):
    return (1/(sd*(2*math.pi))) * math.e ** (-.5 * ((val-mean)/sd) ** 2)
