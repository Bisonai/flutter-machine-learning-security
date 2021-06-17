import unittest

from security import (
    xor_cipher_shuffle,
    load_file,
)


class TestEncryption(unittest.TestCase):
    def test_ecryption_decryption(self):
        orig_file = "README.md"
        enc_file = "README_enc.md"
        xor_cipher_shuffle(
            input_file=orig_file,
            output_file=enc_file,
            encrypt=True,
        )

        dec_file = "README_dec.md"
        xor_cipher_shuffle(
            input_file=enc_file,
            output_file=dec_file,
            encrypt=False,
        )

        orig_content = load_file(orig_file)
        dec_content = load_file(dec_file)
        self.assertEqual(orig_content, dec_content)


if __name__ == '__main__':
    unittest.main()
