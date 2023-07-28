import os
import hashlib
import string
from dotenv import load_dotenv

load_dotenv()

def password_generator(username, length, secret_key):
    # Concatenate the username and the secret key
    input_string = username + secret_key

    # Use SHA256 to generate a deterministic hash
    hash_object = hashlib.sha256(input_string.encode('utf-8'))

    # Create a character set for the password
    chars = string.ascii_letters + string.digits + "!@#$%^&*(),.<>/?"
    print(chars)
    # Convert the hash to a password using the character set
    binary_hash = hash_object.digest()
    password = [chars[b % len(chars)] for b in binary_hash]

    # Trim or pad the password to the desired length
    while len(password) < length:
        password += password
    password = password[:length]

    return ''.join(password)


username = input("Username: ")
length = int(input("Length: "))
secret_key = os.getenv('secret_key')

print(f"Password: {password_generator(username, length, secret_key)}")
