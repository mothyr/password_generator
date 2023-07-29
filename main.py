import os
import hashlib
import string
from dotenv import load_dotenv

load_dotenv()

def password_generator(username, site, length, secret_key):

    if site == None or site == "":

    # Concatenate the username and the secret key
        input_string = username + secret_key
    
    else:
        input_string = username + site + secret_key

    # Use SHA256 to generate a deterministic hash
    hash_object = hashlib.sha256(input_string.encode('utf-8'))

    # Create a character set for the password
    chars = string.ascii_letters + string.digits + "!@#$%^&*(),.<>/?"
    # Convert the hash to a password using the character set
    binary_hash = hash_object.digest()
    password = [chars[b % len(chars)] for b in binary_hash]

    # Trim or pad the password to the desired length
    while len(password) < length:
        password += password
    password = password[:length]

    return ''.join(password)

# Check if secret_key environment variable exists
secret_key = os.getenv('secret_key')
if secret_key is None:
    with open('.env', 'w') as env_file:
        secret_key = input("Please enter a secret key: ")
        env_file.write(f"secret_key={secret_key}\n")
        print("Secret key saved in .env file")

# Load secret key from .env file
load_dotenv()
secret_key = os.getenv('secret_key')

username = input("Username: ")
site = input("Site: ").lower()
length = int(input("Length: "))

print(f"Password: {password_generator(username, site, length, secret_key)}")
