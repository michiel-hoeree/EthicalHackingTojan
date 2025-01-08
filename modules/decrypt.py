from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os



def decrypt_file(key,file_path):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted  = file.read()
    decrypted  = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as dec_file:
        dec_file.write(decrypted)


load_dotenv(dotenv_path='./.env',override=True)
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')            # voor testing heb ik geen env file. daarom kan het zijn dat ik dat manueel moet ingeven


if ENCRYPTION_KEY == "":
    ENCRYPTION_KEY = input("input u key").strip().encode()

key = ENCRYPTION_KEY

file_types = ["docx", "pdf", "csv", "xlsx"]   # , "md", "txt"

# path = "C:/"                     # voor alle files af te runnen ipv 1 file
path = "C:/Users/michi/School/AP/jaar4/ethicalHacking/Deel2/trojan/modules"
for root, dirs, files in os.walk(path):
    for file in files:
        file_path = os.path.join(root, file)
        if file.split(".")[-1] in file_types:
            print(file_path)
            decrypt_file(key,file_path)
