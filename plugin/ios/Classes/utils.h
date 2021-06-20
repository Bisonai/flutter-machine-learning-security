#include <vector>
#include <string>

// outside API
std::vector<unsigned char> xor_cipher(std::vector<unsigned char> message);
std::vector<unsigned char> shuffle_decrypt(std::vector<unsigned char> message);

// inside API
std::vector<unsigned char> load_file(std::string filePath);
std::vector<unsigned char> shuffle_encrypt(std::vector<unsigned char> message);
std::vector<unsigned char> xor_decipher_shuffle(std::string file);
bool compare_messages(std::vector<unsigned char> a, std::vector<unsigned char> b);
