import string
import secrets
print("Random Password Generator Using Python")
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))
print("Password : " + password)