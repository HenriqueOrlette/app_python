import hashlib
import secrets

salt = secrets.token_hex(16)
print(salt)

password = "flamengo"

hash_pass = hashlib.sha256((password + salt).encode())
print(hash_pass.hexdigest())