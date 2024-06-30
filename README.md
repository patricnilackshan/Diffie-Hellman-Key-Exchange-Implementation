# Diffie-Hellman Key Exchange Implementation

This repository contains a Python implementation of the Diffie-Hellman key exchange protocol. The Diffie-Hellman key exchange is a method for securely exchanging cryptographic keys over a public channel and is fundamental in many cryptographic protocols.

### Overview

The implementation uses a 2048-bit prime number and a base (generator) value to generate public and private keys for two parties, A and B. These keys are then used to establish a shared secret code, which can be used for secure communication or further cryptographic operations.

### Usage

#### Prerequisites
- Python 3.x

#### Steps to Use:
1. **Clone the repository:**
```shell
git clone https://github.com/patricnilackshan/Diffie-Hellman-Key-Exchange-Implementation.git
cd Diffie-Hellman-Key-Exchange-Implementation
```


2. **Run the key exchange:**
- Run `python key_exchange.py`.
- Follow the prompts to enter private keys and exchange public keys between Party A and Party B.


3. **Output:**
- After exchanging public keys, the shared secret code (shared secret) will be computed and displayed for each party.


### Files

- `key_exchange.py`: Python script containing the implementation of the key exchange protocol.
- `README.md`: This file, providing an overview of the repository, usage instructions, and explanation of the key exchange process.

### Example

Here's a brief example of how the key exchange works:

1. Party A and Party B each generate their private keys.
2. They exchange their public keys generated from these private keys.
3. Using the exchanged public keys and their own private keys, each party computes the shared secret code.

### Security Note

While this implementation demonstrates the basic principles of the Diffie-Hellman key exchange, real-world applications require careful consideration of additional security measures such as key size, key management, and protection against various attacks (e.g., man-in-the-middle attacks).


### Acknowledgments

- This implementation is inspired by the Diffie-Hellman key exchange protocol and its importance in modern cryptography.

Feel free to explore and use this implementation for educational purposes or as a reference for integrating cryptographic protocols into your projects.
