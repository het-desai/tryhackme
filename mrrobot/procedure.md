# Mr. Robot

## Step 1: Info. Gathering & Enumeration

`sudo nmap -sC -sV -A -O -p- 10.10.177.109`

![nmap result]("")

now here we got ports 80, 443 open and ssh port is closed.

let's copy the IP Address and paste it into the browser and check Developer Window (Inspector, Network, etc.) Tabs.

![home page]("")

This web page gives us to execute some predefined ""COMMAND"", let's check each ""COMMAND""

![prepare]("")

It's a video clip

![fsocity]("")

It's also a video clip

![inform]("")

Its photos and article page

![question]("")

Once again photos.

![wakeup]("")

It's a video clip

![join]("")

it just asks for email and nothing there.

nothing is interesting so let's use the **gobuster** tool.

`gobuster dir -q -t 200 -u http://10.10.177.109 -w /usr/share/dirbuster/wordlist/directory-v2-3-medium.txt`

![gobuster]("")

after this scan, we got some interesting results like default WordPress web pages/directory (wp-content, wp-includes). so let's use another tool **wpscan**.

![WPScan]("")

using this scan result we got our first flag into the **robots.txt** webpage.

![flag 1]("")

there is one more file over there **fsociety.dic**, it is a downloadable file. let's download it and inspect it.

![fsocity]("")

Let's research whats this file is **.dic**

![search result]("")

after the research, it's some kind of text file, so let's open it in nano.

![fsocity file on nano]("")

this file looks like a words list. but wait what's use for. Can we test this list against the **wp-login.php** (Default WordPress Login) page? Let's put the credentials Username: admin & Password: admin. and guess what, it shows something like this.

![login page invalid username]("")

## Step 2: Attack Begin

So let's use the Hydra tool to get the correct username using **fsociety.dic** file. for making hydra payload for WordPress, I took [Refrence]("https://linuxconfig.org/test-wordpress-logins-with-hydra-on-kali-linux")

`hydra -L fsocity.dic -p "" 10.10.205.229 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log In&testcookie=1:S=Invalid Username' -t 10 -V`

![Username brutforce ]("")

Bruteforce the username there is another payload, which you can use in the **Lost your password** page.

`hydra -L fsocity.dic -e n 10.10.205.229 http-post-form '/wp-login.php?action=lostpassword:user_login=^USER^&submit=GET New Password:Invalid username or e-mail' -t 10 -V`

now we have the username, so we need a password. Once again use the hydra

`hydra -l "Elliot" -P fsocity.dic 10.10.205.229 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log In&testcookie=1:S=Location' -t 10 -V`

![Elliot Password]("")

Now we got the username: Elliot & password: ER28-0652, so let's log in and exploit WordPress. This password brute-forcing is too time-consuming so I started the machine twice to find the password. It tests our passions. 

## Step 3: Get the SHELLphone

Let's begin with some exploit research and here I got amazing [Reference]("https://www.hackingarticles.in/wordpress-reverse-shell/"). I recommend to you read all approaches for getting a reverse shell.

![Refrence photo]("")

Now let's apply the Theme Injection Exploit. and once again **PenTest Monkey's** reverse shellcode we use for getting the reverse shell. Make the changes as like IP Address and Port No. and then paste the code into the page **404.php**

![Reverse shell code upload]("")

Now have to set up our net at to listing mode and call any random page using a URL like mention below.

![Page not found page call]("")

Now here we got the reverse shell in our terminal.

![deamon account]("")

let go to **/home/robot/** and here we get our **2nd** flag. but we can't access it so we need to switch the user. there is another file also present **password.raw-md5**. it mentions on the file name the MD5 hash let's find the password using the **John** tool.

`john hash.txt --format=Raw-MD5 -w rockyou.txt`

![robot password]("")

## Step 4: Privilege Enumeration & Escalation

let find some files which contain some SUID permission.

`find / -perm /4000 2>/dev/null`

![SUID Permissioned Files]("")

Here we got a Nmap file, so now we need to check any escalation possible, here I got a reference form [GTFOBins]("https://gtfobins.github.io/gtfobins/nmap/")

![GTFOBins Result]("")

![Apply this method]("")

Bingo!!! Now we got the root access.

THE END!!!