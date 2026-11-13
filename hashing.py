import hashlib, os

print(hashlib.md5(b"password").hexdigest())
# 5f4dcc3b5aa765d61d8327deb882cf99 ← cracked in seconds

def file_sha256(path):  # malware / IOC hash
    with open(path, "rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()

# Passwords: never plain MD5/SHA - use salt + slow KDF
salt = os.urandom(16)
key = hashlib.scrypt(b"S3cret!", salt=salt, n=2**14, r=8, p=1)
print(salt.hex(), key.hex()[:32])
