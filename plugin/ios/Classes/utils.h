#include <vector>
#include <string>

// outside API
std::vector<unsigned char> xor_cipher(std::vector<unsigned char>, int , int, int);
std::vector<unsigned char> shuffle_decrypt(std::vector<unsigned char>, int, int, int);

// inside API
std::vector<unsigned char> load_file(std::string);
std::vector<unsigned char> shuffle_encrypt(std::vector<unsigned char>, int, int, int);
std::vector<unsigned char> xor_decipher_shuffle(std::string, int, int, int, int, int, int);
bool compare_messages(std::vector<unsigned char>, std::vector<unsigned char>);
