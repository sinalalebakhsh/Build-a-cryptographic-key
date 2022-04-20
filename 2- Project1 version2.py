from subprocess import check_output
import os
from cryptography.fernet import Fernet

# os.system('cls')

key = Fernet.generate_key()
print('\n', key)

Encrypt = Fernet(key)

enc_variable = Encrypt.encrypt(b"sina lalebakhsh")
print('\n',enc_variable)



