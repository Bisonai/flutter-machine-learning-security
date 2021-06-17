import unittest

from security import (
    xor_cipher,
    load_file,
)


class TestEncryption(unittest.TestCase):
    def test_ecryption_decryption(self):
        # message = bytearray("bisonai")
        orig_file = "README.md"
        enc_file = "README_enc.md"
        xor_cipher(
            input_file=orig_file,
            output_file=enc_file,
            encrypt=True,
        )

        dec_file = "README_dec.md"
        xor_cipher(
            input_file=enc_file,
            output_file=dec_file,
            encrypt=False,
        )

        orig_content = load_file(orig_file)
        dec_content = load_file(dec_file)
        self.assertEqual(orig_content, dec_content)
    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
