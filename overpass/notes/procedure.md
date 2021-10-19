# Overpass

## Step 1: Enumeration

`nmap -T5 -sC -sV -p- 10.10.223.206`

output:

[Nmap output]()

here port 80 is open with http protocol so, lets open into the browser.

[homepage html comment inspection]()

[homepage with network tab inspection]()

[download page inspection]()

lets download the file look into it.

![source file]()

![application run]()

Here we got nothing special, so lets move on to directory travelsal using **gobuster**

`gobuster dir -q -t 200 -u http://10.10.223.206 -w /usr/share/dirbuster/wordlist/directory-list-2.3-small.txt`

Output:

![gobuster directory output]()

Woooowww, we got some intersting page **/admin**. at first place i tried simple SQLi payload and some simple password but it dosen't work. so lets continue to enumeration part and inspect the html code and network tab.

![admin page html code inspect]()

![admin page network tab]()

In the network tab we got **login.js** this file looks intresting

![login js file]()

## Attack Enumeration Attack

After the JS code inspection, admin code just check SessionToken cookie and this sessiontoken value is dosen't matter so we can put any thing at the place. so edit and resend the admin page with attach fake cookie

![admin page with fake cookie attach]()

here we can successfuly logged-in and we got ssh key with username.

![admin page with ssh key]()

Now we have so try to login into system using this key but it dosen't work.

![ssh login fail]("")

Here we require passphraes. now its time to decrypt the ssh key and get the passphrase using **JohnRepper**

`/usr/share/john/ssh2john id_rsa > ssh2johnhash.txt`

`john ssh2johnhash.txt --wordlist=rockyou.txt`

this last command need to run twice to get the output.

![john output with passphraes]()

Now we can login throw ssh, and we get the out first flag.

![first flag]("")

## Privilege Escalation

first of all we need download **LinPeas.sh** from our machine using python3 server and weget command in taget machine. now run the script and we got some interesting output.

![LinPeas output]("")

this cron job run every minute. its look like download something and run as root user. lets check, Can we edit the **hosts** file? here we got and output. bengo...

![hosts file permission]()

edit the file and replace with our attacking machine IP and setup our machine, make the **buildscript.sh** and host the setver.

![script image]()

![auto download and execute the script]()

Now **/bin/bash** file permission successfuly changed. and now we have root access. so lets finish this session here

![root access and flag]()

THE END!!! :)
