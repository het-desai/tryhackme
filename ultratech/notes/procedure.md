# Ultratech

## Step 1: Enumeration

- Nmap Scan

`nmap -T5 -sV -p- 10.10.10.10 -oN nmap.txt`

[nmap output]()

Open the http ports on browser but there is nothing special, so i decided to enumerate the directory traversal using **gobuster**

First test on Port 8081 

`gobuster dir -u http://10.10.154.187:8081/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -q -t 200`

[gobuster output]()

we got two useful pages **/auth** and **/ping**

this **/auth** page show something weird so, i decided to put some spoof cridentials

[auth page wrong cridentials output]()

i wasted my time too much here then and i took hint

hint: Look closely how the API is used. Don't spend too much time on /auth, it isn't the only route available.

Now i jump on to the second http port web page and run the gobuster again.

Second test on Port 31331

`gobuster dir -u http://10.10.154.187:31331/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -q -t 200`

[gobuster output 31331]()

Output with some juicy pages as mention above in hint

so i directly visit to the **api.js** page. this program look like it executes some command on ping page which we got in previously.

## Attack time

lets try to execute some command on ping page at port 8081

[ping test]()

[ping test with ls]()

[ping test with cat output]()

last command comes up with some hashes

now decrypt the hash using **hashcat**

`hashcat -a 0 hash1.txt --wordlist rockyou.txt`

Username: r00t
Password: **n100906**

With this cridentials i tried to login into port 8081/auth page and this show some useful information regarding server

[]()

lets try to login with ssh and successfuly logged-in

[ssh login in r00t account]()

## Privilege Enumeration and escalation.

First of all we need to download **LinPeas** into the victim machine using the python server and wget command

[LinPeas Output]()

Output with interesting red and yellow marked line. we can run docker command any user account

now visit to the mention below page and i got command for privilege escalation.

[GTFOBins]()

now i have root access so lets ends to this session with finding root private ssh key.
