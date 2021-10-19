# LazyAdmin

## Scanning

`nmap -T4 -n -A -p- 10.10.154.85`

![nmap result]()

here we can see two ports are open port 80 and 22, so open this IP into browser.

## Port 80 Enum

![home page]()

here we got nothing. lets use gobuster for webpage/directory brute forcing

`gobuster dir -u http://10.10.154.85/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -t 100 -q`

![gobuster result 1]()

![content page]()

Here we got **content** page. so lets open it. this web application use SweetRice content management system (CMS). let research about SweetRice exploits.

[exploit-db 40716](https://www.exploit-db.com/exploits/40716)

[exploit-db 40718](https://www.exploit-db.com/exploits/40718)

This Refrence link makes our task easy so lets do gobuster bruteforcing

`gobuster dir -u http://10.10.154.85/content/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -t 100 -q`

![gobuster result 2]()

Now we got some amazing pages so lets check each.

![content images]()

![content js]()

![content themes default]()

![content attachment]()

![content as]()

this **as** page is login page but right now we dont have login cridentials. priviesly got the refrence about **mysql_backup** file so lets check **inc** directory

![content inc]()

and here we got mysql_directory, so visit the directory and download the file and open it into text editor.

![mysql_backup file]()

here we got user name and password hash. this password is look like 32 bit hash must be MD5 hash. so lets try to crack it.

![md5 cracked password]()

Lets test this username and password into **/content/as/** page.

![successfuly login]()

## Port 80 Exploitation Phase

As previesly we got refrence we can upload Arbitory File Upload on target machine so lets try to upload php reverse shell into **media** page. before the upload we need to configure revrse shell and make zip file.

![phpreveseshell]()

![make zip file]()

![upload zip file]()

![successful uploaded]()

And we successfuly upload the file. before open this we page we need to set up **netcat** into own kali/parrot machine. after the setup netcat then open the random named file.

![got user rev shell]()

lets find the user flag

![user flag]()

Now we got the user flag, now we need to get root access.

## WebshellPHONE Privilege Escalation

`sudo -l`

![privilege escalation enum]()

we can execute the **perl** and **copy.sh** as root. this perl script execute system command. in this system command its executes the **copy.sh** file. And this **copy.sh** file try to attemp connect reverse shell to remote port. And we can modify also **copy.sh** file. Now its easy to get root shell. we need to modify the **copy.sh** and replace to attacker IP and change the port no (Optional).

`sudo -u root /usr/bin/perl /home/itguy/backup.pl`

Before execute the **backup.pl** we need to setup over **netcat** listiner mode and the execute the script. After the execute the got the root webshell and we got our final flag **root.txt** flag.

![root flag]()

THE END!!! :)