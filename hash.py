from hashlib import blake2b
def make_password(plaintext):
    h = blake2b(digest_size=20)
    pwd=plaintext.encode()
    h.update(pwd)
    password=h.hexdigest()
    return str(password)
