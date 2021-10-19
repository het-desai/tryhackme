import optparse
import hashlib

password = "0c01f4468bd75d7a84c7eb73846e8d96"
output = ""
wordlist = "/home/parrot/Desktop/toolbox/SecLists/Passwords/Common-Credentials/best110.txt"
salt = "1dac0d92e9fa6bb2"
dict = open(wordlist,"r",encoding='utf-8')
for line in dict.readlines():
    line = line.replace("\n", "")
    print(line)
    step1 = hashlib.md5(str(salt).encode('utf-8') + line.encode('utf-8'))
    step2 = step1.hexdigest()
    if step2 == password:
        output += "\n[+] Password cracked: " + line
        break
dict.close()
print("Final Password: " + output)