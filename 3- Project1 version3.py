from subprocess import check_output
import os
from cryptography.fernet import Fernet

os.system('cls')

key = Fernet.generate_key()
print('\n', key)

encrypt_var = Fernet(key)


enc_variable = encrypt_var.encrypt(b"sina lalebakhsh")
print('\n',enc_variable)

decryption_var = Fernet(key)


dec_variable = decryption_var.decrypt(enc_variable)

print('\n', dec_variable, '\n')




