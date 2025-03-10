import hashlib

mensg1 = "Olá Mundo!"

hash_md5 = hashlib.md5(mensg1.encode())
print(hash_md5.hexdigest())

hash_sha1 = hashlib.sha1(mensg1.encode())
print(hash_sha1.hexdigest())

hash_sha256 = hashlib.sha256(mensg1.encode())
print(hash_sha256.hexdigest())

hash_sha512 = hashlib.sha512(mensg1.encode())
print(hash_sha512.hexdigest())

