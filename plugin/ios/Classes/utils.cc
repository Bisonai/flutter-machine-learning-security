#include <stdint.h>
#include <utility>
#include <fstream>
#include <iterator>
#include <vector>
#include <math.h>
#include <algorithm>
#include <iostream>


class LCG {
private:
    int a;
    int c;
    int m;
    int seed;

public:
    LCG(int _a, int _c, int _m, int _seed) : a(_a), c(_c), m(_m) ,seed(_seed) {}

    int generate() {
        int random = (this->a * this->seed + this->c) % this->m;
        this->seed = random;
        return random;
    }
};


std::vector<unsigned char> xor_cipher(std::vector<unsigned char> message) {
    // FIXME
    int a = 3007;
    int c = 0;
    int m = pow(2, 14) - 3;

    std::vector<unsigned char> message_enc;

    auto msg_size = message.size();
    auto lcg = LCG(a, c, m, msg_size);

    for (auto & msg : message) {
        auto key = lcg.generate();
        message_enc.push_back(msg ^ (key % 256));
    }

    return message_enc;
}

std::vector<unsigned char> load_file(std::string filePath) {
    std::ifstream input(filePath, std::ios::binary);
    std::vector<unsigned char> buffer(std::istreambuf_iterator<char>(input), {});
    return buffer;
}

bool sortbysec(
    const std::pair<int,int> &a,
    const std::pair<int,int> &b)
{
    return (a.second < b.second);
}


std::vector<unsigned char> compose_message(std::vector<unsigned char> message, std::vector<std::pair<int, int>> pairs)
{
    std::vector<unsigned char> new_message;

    for (auto & p: pairs) {
        new_message.push_back(message.at(p.first));
    }

    return new_message;
}

std::vector<std::pair<int,int>> generate_shuffled_pairs(int msg_len) {
    std::vector<std::pair<int,int>> shuffled_pairs;
    int a = 3'007;
    int c = 0;
    int m = pow(2, 14) - 3;
    auto lcg = LCG(a, c, m, msg_len);

    for (auto i = 0; i < msg_len; ++i) {
        shuffled_pairs.push_back(std::make_pair(i, lcg.generate()));
    }

    sort(shuffled_pairs.begin(), shuffled_pairs.end(), sortbysec);

    return shuffled_pairs;
}

std::vector<std::pair<int,int>> generate_decryption_shuffle_pairs(int msg_len, std::vector<std::pair<int, int>> pairs) {
    std::vector<std::pair<int,int>> shuffled_pairs;

    for (auto i = 0; i < msg_len; ++i) {
        shuffled_pairs.push_back(std::make_pair(i, pairs.at(i).first));
    }

    sort(shuffled_pairs.begin(), shuffled_pairs.end(), sortbysec);

    return shuffled_pairs;
}

std::vector<unsigned char> shuffle_encrypt(std::vector<unsigned char> message) {
    auto shuffled_pairs = generate_shuffled_pairs(message.size());
    return compose_message(message, shuffled_pairs);
}

std::vector<unsigned char> shuffle_decrypt(std::vector<unsigned char> message) {
    auto msg_len = message.size();
    auto shuffled_pairs = generate_shuffled_pairs(msg_len);
    auto decryption_shuffle_pairs = generate_decryption_shuffle_pairs(msg_len, shuffled_pairs);
    return compose_message(message, decryption_shuffle_pairs);
}

std::vector<unsigned char> xor_decipher_shuffle(std::string file) {
    auto message_enc_shuffled = load_file(file);
    auto message_shuffled = xor_cipher(message_enc_shuffled);
    return shuffle_decrypt(message_shuffled);
}

bool compare_messages(std::vector<unsigned char> a, std::vector<unsigned char> b) {
    if (a.size() != b.size()) {
        std::cout << "FAIL" << std::endl;
        return false;
    }

    for (auto i = 0; i < a.size(); ++i) {
        if (a.at(i) != b.at(i)) {
            std::cout << "FAIL" << std::endl;
            return false;
        }
    }

    std::cout << "OK" << std::endl;
    return true;
}
