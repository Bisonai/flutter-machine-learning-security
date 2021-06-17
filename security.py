"""
XOR - cipher

References:
[1] https://en.wikipedia.org/wiki/Linear_congruential_generator
[2] https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=37999C8E99C9D0F67EF7E6F714AF8065?doi=10.1.1.34.1024&rep=rep1&type=pdf
[3] https://en.wikipedia.org/wiki/XOR_cipher
"""
from typing import (
    Dict,
    Generator,
    List,
    Tuple,
)
from pathlib import Path
from argparse import ArgumentParser

# Values taken from page 5 at [2]
XOR_KEY = {
    "m": (2 ** 14) - 3,
    "a": 3_007,
    "c": 0,
}


SHUFFLE_KEY = {
    "m": (2 ** 14) - 3,
    "a": 3_007,
    "c": 0,
}


def lcg(seed: int, key: Dict[str, int]) -> Generator[int, None, None]:
    """Linear congruential generator.
    """
    while True:
        seed = (key["a"] * seed + key["c"]) % key["m"]
        yield seed


def load_file(filename: Path) -> List[int]:
    with open(filename, "rb") as f:
        return list(f.read())


def save_file(message: List[int], filename: Path) -> None:
    with open(filename, "wb") as f:
        f.write(bytearray(message))


def generate_shuffled_pairs(len_msg: int) -> List[Tuple[int, int]]:
    """Generate pairs of number consisting of an increasing sequence
    of numbers and pseudo-randomly generated numbers. Sort pairs based
    on the pseudo-random numbers.

    Before shuffling
    | i |  r |
    |---+----|
    | 0 | 10 |
    | 1 |  7 |
    | 2 | 33 |
    | 4 | 12 |

    After shuffling
    | i |  r |
    |---+----|
    | 1 |  7 |
    | 0 | 10 |
    | 4 | 12 |
    | 2 | 33 |
    """
    return sorted(
        [
            (i, r)
            for i, r in zip(range(len_msg), lcg(len_msg, SHUFFLE_KEY))
        ],
        key=lambda p: p[1],
    )


def generate_decryption_shuffle_pairs(len_msg: int, shuffled_pairs: List[int]) -> List[Tuple[int, int]]:
    """
    Shuffled pairs
    | i |  r |
    |---+----|
    | 1 |  7 |
    | 0 | 10 |
    | 4 | 12 |
    | 2 | 33 |
    """
    return sorted(
        [
            (i, r)
            for i, r in zip(range(len_msg), [p[0] for p in shuffled_pairs])
        ],
        key=lambda p: p[1],
    )


def compose_message(message: List[int], pairs: List[Tuple[int, int]]):
    return [message[p[0]] for p in pairs]


def shuffle_encrypt(message: List[int]) -> List[int]:
    len_msg = len(message)
    shuffled_pairs = generate_shuffled_pairs(len_msg)
    return compose_message(message, shuffled_pairs)


def shuffle_decrypt(message: List[int]) -> List[int]:
    len_msg = len(message)
    shuffled_pairs = generate_shuffled_pairs(len_msg)
    decryption_shuffle_pairs = generate_decryption_shuffle_pairs(
        len_msg,
        shuffled_pairs,
    )
    return compose_message(message, decryption_shuffle_pairs)


def xor_cipher(message: List[int]) -> List[int]:
    return [
        msg ^ (key % 256)
        for msg, key in zip(message, lcg(len(message), XOR_KEY))
    ]


def xor_cipher_shuffle(
    input_file: Path,
    output_file: Path,
    encrypt: bool,
):
    decrypt = not encrypt
    message_in = load_file(input_file)

    if encrypt:
        message_in = shuffle_encrypt(message_in)

    message_out = xor_cipher(message_in)

    if decrypt:
        message_out = shuffle_decrypt(message_out)

    save_file(message_out, output_file)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--input_file", type=Path)
    parser.add_argument("--output_file", type=Path)
    parser.add_argument("--encrypt", dest="encrypt", action="store_true")
    parser.add_argument("--decrypt", dest="encrypt", action="store_false")
    args = parser.parse_args()

    xor_cipher_shuffle(
        args.input_file,
        args.output_file,
        args.encrypt,
    )
