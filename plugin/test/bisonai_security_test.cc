#include <vector>
#include "utils.h"
#include <cmath>


const int a_key = 3'007;
const int c_key = 0;
const int m_key = pow(2, 14) - 3;

const int a_shuffle = 3'007;
const int c_shuffle = 0;
const int m_shuffle = pow(2, 14) - 3;


bool test_decryption() {
    auto msg_orig = load_file("../../../README.md");
    auto msg_dec = xor_decipher_shuffle(
        "../../../README_enc.md",
        a_key,
        c_key,
        m_key,
        a_shuffle,
        c_shuffle,
        m_shuffle
        );
    return compare_messages(msg_orig, msg_dec);
}

bool test_string_encryption_decryption() {
    std::vector<unsigned char> msg_orig;
    msg_orig.push_back('b');
    msg_orig.push_back('i');
    msg_orig.push_back('s');
    msg_orig.push_back('o');
    msg_orig.push_back('n');
    msg_orig.push_back('a');
    msg_orig.push_back('i');

    auto msg = shuffle_encrypt(
        msg_orig,
        a_shuffle,
        c_shuffle,
        m_shuffle
        );
    msg = xor_cipher(
        msg,
        a_key,
        c_key,
        m_key
        );

    msg = xor_cipher(
        msg,
        a_key,
        c_key,
        m_key
        );
    auto msg_dec = shuffle_decrypt(
        msg,
        a_shuffle,
        c_shuffle,
        m_shuffle
        );

    return compare_messages(msg_orig, msg_dec);
}

int main() {
    test_string_encryption_decryption();
    test_decryption();
}
