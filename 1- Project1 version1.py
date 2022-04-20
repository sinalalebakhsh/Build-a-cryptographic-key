from subprocess import check_output
import os
from cryptography.fernet import Fernet

# os.system('cls')

key = Fernet.generate_key()

print(key)



