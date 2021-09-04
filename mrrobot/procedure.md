# Mr. Robot

## Step 1: Info. Gathering & Enumeration

`sudo nmap -sC -sV -A -O -p- 10.10.177.109`

![nmap result](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/nmap.png)

now here we got ports 80, 443 open and ssh port is closed.

let's copy the IP Address and paste it into the browser and check Developer Window (Inspector, Network, etc.) Tabs.

![home page](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/home%20web%20page.png)

This web page gives us to execute some predefined ""COMMAND"", let's check each ""COMMAND""

![prepare](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/prepare.png)

It's a video clip

![fsocity](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/fsociety.png)

It's also a video clip

![inform](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/inform.png)

Its photos and article page

![question](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/question.png)

Once again photos.

![wakeup](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/wakeup%20video.png)

It's a video clip

![join](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/join.png)

it just asks for email and nothing there.

nothing is interesting so let's use the **gobuster** tool.

`gobuster dir -q -t 200 -u http://10.10.177.109 -w /usr/share/dirbuster/wordlist/directory-v2-3-medium.txt`

![gobuster](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/gobuster.png)

after this scan, we got some interesting results like default WordPress web pages/directory (wp-content, wp-includes). so let's use another tool **wpscan**.

![WPScan](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/wpscan.png)

using this scan result we got our first flag into the **robots.txt** webpage.

![flag 1](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/robots.png)

there is one more file over there **fsociety.dic**, it is a downloadable file. let's download it and inspect it.

Let's research whats this file is **.dic**

![search result](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/dic%20infomation.png)

after the research, it's some kind of text file, so let's open it in nano.

![fsocity file](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/fsoc%20dic.png)

this file looks like a words list. but wait what's use for. Can we test this list against the **wp-login.php** (Default WordPress Login) page? Let's put the credentials Username: admin & Password: admin. and guess what, it shows something like this.

![login page invalid username](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/login%20page%20username%20bug.png)

## Step 2: Attack Begin

So let's use the Hydra tool to get the correct username using **fsociety.dic** file. for making hydra payload for WordPress, I took [Refrence]("https://linuxconfig.org/test-wordpress-logins-with-hydra-on-kali-linux")

`hydra -L fsocity.dic -p "" 10.10.205.229 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log In&testcookie=1:S=Invalid Username' -t 10 -V`

![Username brutforce ](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/hydra%20with%20username%20test.png)

Bruteforce the username there is another payload, which you can use in the **Lost your password** page.

`hydra -L fsocity.dic -e n 10.10.205.229 http-post-form '/wp-login.php?action=lostpassword:user_login=^USER^&submit=GET New Password:Invalid username or e-mail' -t 10 -V`

now we have the username, so we need a password. Once again use the hydra

`hydra -l "Elliot" -P fsocity.dic 10.10.205.229 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log In&testcookie=1:S=Location' -t 10 -V`

![Elliot Password](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/hydra%20found%20password.png)

Now we got the username: Elliot & password: ER28-0652, so let's log in and exploit WordPress. This password brute-forcing is too time-consuming so I started the machine twice to find the password. It tests our passions. 

## Step 3: Get the SHELLphone

Let's begin with some exploit research and here I got amazing [Reference]("https://www.hackingarticles.in/wordpress-reverse-shell/"). I recommend to you read all approaches for getting a reverse shell.

![Refrence photo](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/reveseshell%20exploit%20reference.png)

Now let's apply the Theme Injection Exploit. and once again **PenTest Monkey's** reverse shellcode we use for getting the reverse shell. Make the changes as like IP Address and Port No. and then paste the code into the page **404.php**

![Reverse shell code upload](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/404%20page%20script%20change.png)

Now have to set up our net at to listing mode and call any random page using a URL like mention below.

![Page not found page call](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/error%20page%20call.png)

Now here we got the reverse shell in our terminal.

![deamon account](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/daemon%20user%20access.png)

let go to **/home/robot/** and here we get our **2nd** flag. but we can't access it so we need to switch the user. there is another file also present **password.raw-md5**. it mentions on the file name the MD5 hash let's find the password using the **John** tool.

`john hash.txt --format=Raw-MD5 -w rockyou.txt`

![robot password](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/john.png)

## Step 4: Privilege Enumeration & Escalation

let find some files which contain some SUID permission.

`find / -perm /4000 2>/dev/null`

![SUID Permissioned Files](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/file%20SUID%20permission.png)

Here we got a Nmap file, so now we need to check any escalation possible, here I got a reference form [GTFOBins]("https://gtfobins.github.io/gtfobins/nmap/")

![GTFOBins Result](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/GTFOBins.png)

![Apply this method](https://github.com/xzeroo/tryhackme/blob/main/mrrobot/procedure/root%20access.png)

Bingo!!! Now we got the root access.

THE END!!!
