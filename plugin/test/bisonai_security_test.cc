#include <vector>
#include "utils.h"


bool test_decryption() {
    auto msg_orig = load_file("../../../README.md");
    auto msg_dec = xor_decipher_shuffle("../../../README_enc.md");
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

    auto msg = shuffle_encrypt(msg_orig);
    msg = xor_cipher(msg);

    msg = xor_cipher(msg);
    auto msg_dec = shuffle_decrypt(msg);

    return compare_messages(msg_orig, msg_dec);
}

int main() {
    test_string_encryption_decryption();
    test_decryption();
}
