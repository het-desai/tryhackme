# THM: Bolt

## Intitial Scan

`nmap -sCV -oN nmap.init 10.10.1.153`

```
# Nmap 7.93 scan initiated Wed Dec 27 09:31:18 2023 as: nmap -sCV -oN nmap.init 10.10.139.57
Nmap scan report for 10.10.139.57
Host is up (0.042s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f385ec54f201b19440de42e821972080 (RSA)
|   256 77c7c1ae314121e4930e9add0b29e1ff (ECDSA)
|_  256 070543469db23ef04d6967e491d3d37f (ED25519)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
8000/tcp open  http    (PHP 7.2.32-1)
|_http-generator: Bolt
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 Not Found
|     Date: Wed, 27 Dec 2023 09:31:33 GMT
|     Connection: close
|     X-Powered-By: PHP/7.2.32-1+ubuntu18.04.1+deb.sury.org+1
|     Cache-Control: private, must-revalidate
|     Date: Wed, 27 Dec 2023 09:31:33 GMT
|     Content-Type: text/html; charset=UTF-8
|     pragma: no-cache
|     expires: -1
|     X-Debug-Token: 2b9536
|     <!doctype html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <title>Bolt | A hero is unleashed</title>
|     <link href="https://fonts.googleapis.com/css?family=Bitter|Roboto:400,400i,700" rel="stylesheet">
|     <link rel="stylesheet" href="/theme/base-2018/css/bulma.css?8ca0842ebb">
|     <link rel="stylesheet" href="/theme/base-2018/css/theme.css?6cb66bfe9f">
|     <meta name="generator" content="Bolt">
|     </head>
|     <body>
|     href="#main-content" class="vis
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Wed, 27 Dec 2023 09:31:33 GMT
|     Connection: close
|     X-Powered-By: PHP/7.2.32-1+ubuntu18.04.1+deb.sury.org+1
|     Cache-Control: public, s-maxage=600
|     Date: Wed, 27 Dec 2023 09:31:33 GMT
|     Content-Type: text/html; charset=UTF-8
|     X-Debug-Token: e0ac47
|     <!doctype html>
|     <html lang="en-GB">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <title>Bolt | A hero is unleashed</title>
|     <link href="https://fonts.googleapis.com/css?family=Bitter|Roboto:400,400i,700" rel="stylesheet">
|     <link rel="stylesheet" href="/theme/base-2018/css/bulma.css?8ca0842ebb">
|     <link rel="stylesheet" href="/theme/base-2018/css/theme.css?6cb66bfe9f">
|     <meta name="generator" content="Bolt">
|     <link rel="canonical" href="http://0.0.0.0:8000/">
|     </head>
|_    <body class="front">
|_http-title: Bolt | A hero is unleashed
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8000-TCP:V=7.93%I=7%D=12/27%Time=658BEEF3%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,28ED,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Wed,\x2027\x20Dec\x2
SF:02023\x2009:31:33\x20GMT\r\nConnection:\x20close\r\nX-Powered-By:\x20PH
SF:P/7\.2\.32-1\+ubuntu18\.04\.1\+deb\.sury\.org\+1\r\nCache-Control:\x20p
SF:ublic,\x20s-maxage=600\r\nDate:\x20Wed,\x2027\x20Dec\x202023\x2009:31:3
SF:3\x20GMT\r\nContent-Type:\x20text/html;\x20charset=UTF-8\r\nX-Debug-Tok
SF:en:\x20e0ac47\r\n\r\n<!doctype\x20html>\n<html\x20lang=\"en-GB\">\n\x20
SF:\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20charset=\"
SF:utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20name=\"viewport\"\x2
SF:0content=\"width=device-width,\x20initial-scale=1\.0\">\n\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<title>Bolt\x20\|\x20
SF:A\x20hero\x20is\x20unleashed</title>\n\x20\x20\x20\x20\x20\x20\x20\x20<
SF:link\x20href=\"https://fonts\.googleapis\.com/css\?family=Bitter\|Robot
SF:o:400,400i,700\"\x20rel=\"stylesheet\">\n\x20\x20\x20\x20\x20\x20\x20\x
SF:20<link\x20rel=\"stylesheet\"\x20href=\"/theme/base-2018/css/bulma\.css
SF:\?8ca0842ebb\">\n\x20\x20\x20\x20\x20\x20\x20\x20<link\x20rel=\"stylesh
SF:eet\"\x20href=\"/theme/base-2018/css/theme\.css\?6cb66bfe9f\">\n\x20\x2
SF:0\x20\x20\t<meta\x20name=\"generator\"\x20content=\"Bolt\">\n\x20\x20\x
SF:20\x20\t<link\x20rel=\"canonical\"\x20href=\"http://0\.0\.0\.0:8000/\">
SF:\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<body\x20class=\"front\">\n\
SF:x20\x20\x20\x20\x20\x20\x20\x20<a\x20")%r(FourOhFourRequest,16C3,"HTTP/
SF:1\.0\x20404\x20Not\x20Found\r\nDate:\x20Wed,\x2027\x20Dec\x202023\x2009
SF::31:33\x20GMT\r\nConnection:\x20close\r\nX-Powered-By:\x20PHP/7\.2\.32-
SF:1\+ubuntu18\.04\.1\+deb\.sury\.org\+1\r\nCache-Control:\x20private,\x20
SF:must-revalidate\r\nDate:\x20Wed,\x2027\x20Dec\x202023\x2009:31:33\x20GM
SF:T\r\nContent-Type:\x20text/html;\x20charset=UTF-8\r\npragma:\x20no-cach
SF:e\r\nexpires:\x20-1\r\nX-Debug-Token:\x202b9536\r\n\r\n<!doctype\x20htm
SF:l>\n<html\x20lang=\"en\">\n\x20\x20\x20\x20<head>\n\x20\x20\x20\x20\x20
SF:\x20\x20\x20<meta\x20charset=\"utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x
SF:20<meta\x20name=\"viewport\"\x20content=\"width=device-width,\x20initia
SF:l-scale=1\.0\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20<title>Bolt\x20\|\x20A\x20hero\x20is\x20unleashed</title>\n\x
SF:20\x20\x20\x20\x20\x20\x20\x20<link\x20href=\"https://fonts\.googleapis
SF:\.com/css\?family=Bitter\|Roboto:400,400i,700\"\x20rel=\"stylesheet\">\
SF:n\x20\x20\x20\x20\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"
SF:/theme/base-2018/css/bulma\.css\?8ca0842ebb\">\n\x20\x20\x20\x20\x20\x2
SF:0\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"/theme/base-2018/css/the
SF:me\.css\?6cb66bfe9f\">\n\x20\x20\x20\x20\t<meta\x20name=\"generator\"\x
SF:20content=\"Bolt\">\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<body>\n\
SF:x20\x20\x20\x20\x20\x20\x20\x20<a\x20href=\"#main-content\"\x20class=\"
SF:vis");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Dec 27 09:31:42 2023 -- 1 IP address (1 host up) scanned in 24.92 seconds
```

Port 8000 is open. The home page has a username and password in the web page posts. I searched for web technology and found the web application built on Bolt CMS.

![Password](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/password.png)

![Username and Website CMS Copyright tag](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/usernameAndCMSName.png)

## Search technology information over Internet

Search for details about CMS. I found that Bolt CMS's has default login pages.

![Bolt web page research](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/webpageResearch.png)

## Get initial access

Test user credentials at the login page, and credentials successfully worked. The version of Bolt CMS, which is mentioned at the bottom of the dashboard.

![CMS version](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/cmsVersion.png)

## Search exploit for Bolt CMS

Search Bolt CMS exploits in the Google Hacking Database using the terminal tool.

`searchsploit bolt`

![Google hacking database exploit ID](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/cmsVulnerabilityGhdb.png)

Detailed explanation about the exploit mentioned [here](https://github.com/het-desai/tryhackme/blob/main/bolt/Bolt.md#Exploit%20explaination). Search the exploit on Metasploit as well.

`search bolt`

![Metasploit exploit module name for Bolt CMS](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/cmsVulnerabilityMetasploit.png)

## Exploit the target

Use the `exploit/unix/webapp/bolt_authenticated_rce` exploit and configure LHOST, LPORT, RHOST, RPORT, Username, Password and the run the exploit. Successful exploit gives a webshell into our terminal.

![Metasploit exploit execution](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/cmsExploitExecution.png)

## Exploit explaination

Here, I only use snapshots of the code to explain the vulnerability. The complete code is [here](https://www.exploit-db.com/exploits/48296).

### Part 1

After the dashboard access, anyone can execute a remote command. The profile page has Display name component, which is our web shell upload point. In the below code, you can see that the display name has a PHP web shell code in the POST request data.

![Exploit Part 1](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/exploitP1.png)

All this session information is stored in a random name file, which you can visit by following this path.

`http://targeted.website/async/browser/cache/.session`

![Exploit Part 2](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/exploitP2.png)

The below screenshot shows that in the system, the display name is stored.

![Exploit Part 3](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/exploitP3.png)

The Dashboard > File Management page has rename functionality, where you get an idea of how this CMS uses the rename functionality. Same way in the below script use and rename the session file. Not only rename the file, but also change the location of the file using path traverse.

![Exploit Part 4](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/exploitP4.png)

After that, rename the file and change the file location on the File Management page. Now its time to execute the command below screenshot.

![Exploit Part 5](https://github.com/het-desai/tryhackme/blob/main/bolt/photos/exploitP5.png)

**Disclamer: Above screenshot there are multiple machine IPs because I started machine twice to take screenshots.**