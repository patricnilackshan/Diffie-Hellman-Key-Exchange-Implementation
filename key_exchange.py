g = 2  # Base (generator), a very big integer
m = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E08"
         "8A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD"
         "3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7E"
         "C6F44C42E9A63A36210000000000090563", 16)  # Large prime number (2048-bit)

def calculate_public_key(private_key):
    """Calculate and return the public key based on the private key."""
    return pow(g, private_key, m)

def calculate_secret_code(other_party_public_key, private_key):
    """Calculate and return the shared secret based on the other party's public key."""
    return pow(other_party_public_key, private_key, m)

# Party A: Generate private key and public key
private_a = int(input("Party A: Enter your private key: "))
public_a = calculate_public_key(private_a)
print("Party A: Share this key with Party B:", public_a, "\n")

# Party B: Generate private key and public key
private_b = int(input("Party B: Enter your private key: "))
public_b = calculate_public_key(private_b)
print("Party B: Share this key with Party A:", public_b, "\n")

# Party A: Receive Party B's public key and calculate shared secret
shared_key_b = int(input("Party A: Enter Party B's public key: "))
secret_code_a = calculate_secret_code(shared_key_b, private_a)
print("Party A: Secret Code (shared secret) is:", secret_code_a, "\n")

# Party B: Receive Party A's public key and calculate shared secret
shared_key_a = int(input("Party B: Enter Party A's public key: "))
secret_code_b = calculate_secret_code(shared_key_a, private_b)
print("Party B: Secret Code (shared secret) is:", secret_code_b, "\n")
