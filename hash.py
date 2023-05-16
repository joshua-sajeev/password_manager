import bcrypt

def make_password(plaintext):
    salt=bcrypt.gensalt()
    pw=plaintext.encode('ASCII')
    password=bcrypt.hashpw(pw,salt)
    return str(password)


