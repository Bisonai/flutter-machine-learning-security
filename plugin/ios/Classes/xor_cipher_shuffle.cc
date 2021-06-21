#include <stdint.h>

#include "utils.h"

extern "C" __attribute__((visibility("default"))) __attribute__((used))
unsigned char* xor_cipher_shuffle(
    unsigned char* message,
    int len,
    int a_key,
    int c_key,
    int m_key,
    int a_shuffle,
    int c_shuffle,
    int m_shuffle
    ) {
    std::vector<unsigned char> message_vec;

    for (int i = 0; i < len; ++i) {
        message_vec.push_back(message[i]);
    }

    auto message_shuffled = xor_cipher(
        message_vec,
        a_key,
        c_key,
        m_key);

    auto message_dec = shuffle_decrypt(
        message_shuffled,
        a_shuffle,
        c_shuffle,
        m_shuffle);

    unsigned char * out = (unsigned char *)malloc(len * sizeof(unsigned char));

    for (int i = 0; i < len; ++i) {
        out[i] = message_dec.at(i);
    }

    return out;
}

extern "C" __attribute__((visibility("default"))) __attribute__((used))
void free_string(unsigned char * str) {
    free(str);
}
