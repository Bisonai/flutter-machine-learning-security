#include <stdint.h>

#include "utils.h"

extern "C" __attribute__((visibility("default"))) __attribute__((used))
unsigned char* xor_cipher_shuffle(unsigned char* message, int len) {
    std::vector<unsigned char> message_vec;
    for (int i = 0; i < len; ++i) {
        message_vec.push_back(message[i]);
    }

    auto message_shuffled = xor_cipher(message_vec);
    auto message_dec = shuffle_decrypt(message_shuffled);

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
