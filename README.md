## Bisonai Security

This repository contains techniques for encryption and decryption of machine learning models.
Machine learning models deployed on mobile devices are vulnerable without a proper encryption techniques.

### Pseudo-random generator

https://en.wikipedia.org/wiki/Linear_congruential_generator

https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=37999C8E99C9D0F67EF7E6F714AF8065?doi=10.1.1.34.1024&rep=rep1&type=pdf

### XOR cipher

https://en.wikipedia.org/wiki/XOR_cipher


### Example Usage

```python
python3 security.py \
    --input_file README.md \
    --output_file README_enc.md

python3 security.py \
    --input_file README_enc.md \
    --output_file README_dec.md

diff README.md README_dec.md
```
