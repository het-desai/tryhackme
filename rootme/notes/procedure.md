# RootMe

## Step 1: Enumeration

`nmap -T5 -sC -sV -p 0-1000 10.10.113.5`

Output:

![nmap result]("")

here we got port 80 and 22 open. Now lets open the IP Address on browser. as we prefer to question then we need to scan the file using gobuster

`gobuster dir -q -t 200 -u http://10.10.113.5 -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt`

Output:

![gobuster result]("")

this **panel** page is looks interseting, here we can upload file reverse shell file. 

## Step 2: Exploit the target

lets try to upload pentestmonkey with changes IP Address and Port no. after the changes, now i tried to upload **phpfile.php** (reverse shell) file but it dosn't work. 

![phpreverseshell fail to upload]("")

show i tied to change file extention **phpfile.phtml** and successfully uploaded. so now before to run the file we need to set our netcat listener. according which we set port on phpfile.phtml file.

![phtml upload file]("")

![Successfuly upload file]("")

Now we got user shell on our terminal. and find the user flag.

`find / -name "user.txt" 2>/dev/null`

![user shell access]("")

## Step 3: Privilege Enumeration & Escalation

Lets try to get root access. first of all download **LinPeas.sh** on victim machine using python http server and wget command. after download the **LinPeas.sh** change the permission to set to execute and run the script.

![LinPeas imp output]("")

here we got python have special permission, lets check the exploit on [GTFOBins]("https://gtfobins.github.io/gtfobins/python/#suid") here we got our payload.

![GTFOBins Webpage]("")

now to run the payload and we got root shell. now lets find the **root.txt** flag.

`find / -name "root.txt" 2>/dev/null`

![root access]("")

THE END!!!