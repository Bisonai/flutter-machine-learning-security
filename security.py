"""
XOR - cipher

References:
[1] https://en.wikipedia.org/wiki/Linear_congruential_generator
[2] https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=37999C8E99C9D0F67EF7E6F714AF8065?doi=10.1.1.34.1024&rep=rep1&type=pdf
[3] https://en.wikipedia.org/wiki/XOR_cipher
"""
from typing import Generator
from pathlib import Path
from argparse import ArgumentParser

# TODO add shuffling


def lcg(seed: int) -> Generator[int, None, None]:
    """Linear congruential generator.
    """
    # Values taken from page 5 at [2]
    m: int = (2 ** 14) - 3
    a: int = 3_007
    c: int = 0

    while True:
        seed = (a * seed + c) % m
        yield seed


def load_file(filename: Path) -> bytes:
    with open(filename, "rb") as f:
        return f.read()


def save_file(content: bytes, filename: Path) -> None:
    with open(filename, "wb") as f:
        return f.write(content)


def xor_cipher(args):
    content_in = load_file(args.input_file)

    content_out = bytearray([
        msg ^ (key % 256)
        for msg, key in zip(content_in, lcg(len(content_in)))
    ])

    save_file(content_out, args.output_file)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--input_file", type=Path)
    parser.add_argument("--output_file", type=Path)
    args = parser.parse_args()
    xor_cipher(args)
