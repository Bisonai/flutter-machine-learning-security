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


def load_file(filename: Path) -> bytes:
    with open(filename, "rb") as f:
        return f.read()


def save_file(content: bytes, filename: Path) -> None:
    with open(filename, "wb") as f:
        return f.write(content)


def shuffle(arr: bytearray, encrypt: bool) -> List:
    len_arr = len(arr)
    pairs = [
        (idx, r)
        for idx, r in zip(range(len_arr), lcg(len_arr, SHUFFLE_KEY))
    ]
    shuffled_pairs = sorted(pairs, key=lambda x: x[1])

    if not encrypt:
        pairs = [
            (idx, r)
            for idx, r in zip(range(len_arr), [s for s, _ in shuffled_pairs])
        ]
        shuffled_pairs = sorted(pairs, key=lambda x: x[1])

    return [arr[i] for i, _ in shuffled_pairs]


def xor_cipher(args):
    content_in = load_file(args.input_file)

    if args.encrypt:
        content_in = shuffle(content_in, args.encrypt)

    content_out = bytearray([
        msg ^ (key % 256)
        for msg, key in zip(content_in, lcg(len(content_in), XOR_KEY))
    ])

    if not args.encrypt:
        content_out = bytearray(shuffle(content_out, args.encrypt))

    save_file(content_out, args.output_file)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--input_file", type=Path)
    parser.add_argument("--output_file", type=Path)
    parser.add_argument("--encrypt", dest="encrypt", action="store_true")
    parser.add_argument("--decrypt", dest="encrypt", action="store_false")
    args = parser.parse_args()
    xor_cipher(args)
