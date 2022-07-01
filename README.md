## Flutter Machine Learning Security

This repository contains techniques for encryption and decryption of machine learning models.
Machine learning models deployed on mobile devices are vulnerable to a theft without a proper encryption techniques.

Flutter Bisonai Security plugin is located inside plugin directory.


### Example Usage

```bash
python3 security.py \
    --encrypt \
    --input_file README.md \
    --output_file README_enc.md

python3 security.py \
    --decrypt \
    --input_file README_enc.md \
    --output_file README_dec.md

diff README.md README_dec.md
```

## Unit tests

```python
python -m unittest security_test
```


## Flutter plugin

### Test

```bash
cd plugin/test
mkdir build && cd build
cmake ..
make
./BisonaiSecurityTest
```

## Resources

* https://en.wikipedia.org/wiki/Linear_congruential_generator
* https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=37999C8E99C9D0F67EF7E6F714AF8065?doi=10.1.1.34.1024&rep=rep1&type=pdf
* https://en.wikipedia.org/wiki/XOR_cipher
