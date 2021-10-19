# Acttacktive Directory

## Step 1: Tools and Scripts Requirements

1. [impacket]("https://github.com/SecureAuthCorp/impacket")

2. [kerbrute]("https://github.com/ropnop/kerbrute/releases")

## Step 2: Enumeratation

- scan the ports and domain name using nmap

`nmap -A -p- 10.10.189.50`

- now we got the domain name **spookysec.local** and useful ports and services are running is on.

- now enumerate deeply using kerbrut tool with given usernames and check which user is present in AD

`kerbrute userenum -d spookysec.local --dc 10.10.189.50 uname.txt`

- Here we got bunch of users list

**Note: It is NOT recommended to brute force credentials due to account lockout policies that we cannot enumerate on the domain controller.**

## Step 3: Abuse target

- we can attempt to abuse a feature within Kerberos with an attack method called ASREPRoasting. ASReproasting occurs when a user account has the privilege "Does not require Pre-Authentication" set. This means that the account does not need to provide valid identification before requesting a Kerberos Ticket on the specified user account.

- Impacket has a tool called "GetNPUsers.py".

- GetNPUsers.py allow us to query ASReproastable accounts from the Key Distribution Center. The only thing that's necessary to query accounts is a valid set of usernames which we enumerated previously via Kerbrute.

`GetNPUsers.py spookysec.local/svc-admin -no-pass`

- Woooow, we got an long hash string.

- Now decrypt the hash using john repper tool and we will get password **management2005**

## Step 4: Back to Basic Enumeration

- Now we have username and password, so try to get some information from that account using `smbclient`.

`smbclient -L 10.10.189.50 -U svc-admin`

- It will show up some useful directories, like Admin, IPC, C, NETLOGON, SYSVOL, backup this all are normal to be there except one backup.

- this backup directory have some important file **backup_credentials.txt**

- There is base64 string is look like, after the dcrypt we got a username with password **backup@spookysec.local:backup2517860**

## Step 5: Elevating Privileges with the Domain

- Using this cridintial try to login into that account.

- we can successfuly login but we can't get the access of the administrator account or we can't dump the other users passwords.

- So try to dump the password of other users.

`secretsdump.py spookysec.local/backup:"backup2517860"@10.10.189.50 -just-dc`

- Now we got the hashes from "backup" user.

- Now simply pass the username and hash in `psexec.py`

`psexec.py Administrator@10.10.189.50 -hashes ajhsdjfahsdjfgajsdfkjashdkf:ajsgdjfhakjsdgfkjasgdfkjh`

- And we get access to the administrator account.
