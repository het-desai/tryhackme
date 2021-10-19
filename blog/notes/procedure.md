# Blog Procuder

## Step 1: Enumeration

As always nmap scan with this command

`nmap -sC -sV -A -O -p- -oN nmap.txt 10.10.59.163`

Output:

[nmap scan result]("")

here we get smb port with vulnerable share file access. so lets enumerate to the SMB port using enum4linux

`enum4linux 10.10.254.106`

output is so long so, i just snipt some usefull part of snapshot

[enum4linux scan result]("")

## Step 2: Exploit

we got an share file **BillySMB** without any protection. so lets test it.

`smbclient //10.10.10.1/BillySMB -U Anonmys` -p 445`

[SMB logged-in output]()

after checking this three file i am so disapointed because its rabbit hole. at the first place i dont know whats hidden in this file so i leave it but after successfuly completed this challenge so I read write-ups about this challenge here i see some stagnograpy is also used. but any way this is also not even useful if i got at the first place. here is writeup link [writeup link]()

## Step 3: Enumeration and Research

now lets move on, we need some real stuff, now we scan port 80 using wpscan

`wpscan --url http://blog.thm/ -e u`

[wpscan result 1]("")

here we got some username so lets try to crack the password again using wpscan

`wpscan --url http://blog.thm/ -e u -U kwheel -P rockyou.txt`

[wpscan with password]("")

after getting username and password lets try to login into the wordpress login page. we can successfuly logged-in. But we can not find anything special, so once again check our wpscan output and here we can Wordpress version no. so i decided to google it and I got and exploit using metasploit. exploit name `Crop-Image`.

## Step 4: Once angain Exploit beggien and little bit research

Now it time use metasploit.

[Metasploit exploit options]()

after looking options we  already have username and password so now easy to get basic access.

[metasploit shell connected]("")

after the getting the shell i directly go to the users home directory and there is **user.txt** but its a fake file. so i decide to go to find some special permissions files using find command.

`find / -perm -u=s 2>/dev/null`

[list of files]()

here we got some bunch of file list. at the first time waste too much time and i dont know which file is suspicous, so once again need some research, and after the research i come up with **checker** binery file which is not by default so i download it in my own machine and put it into gidra software.

[gidra output]()

its basic C program file. Which is acutaly check the admin path and if its empty then it dont give the root shell. Its so simple. we need to add anything in admin variable path and it will give us root shell.

`export admin=hello`

and run the binary file

`/usr/sbin/checker`

and now we got the root access. now once again it time to use **find** command.

`find / -name user.txt 2>/dev/null`

`find / -name root.txt 2>/dev/null`

THE END!!! :)
