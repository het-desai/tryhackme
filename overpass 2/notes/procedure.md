# Overpass 2

## Step 1: Analyse the PCAP

We have **.pcapng**, lets open into wireshark tool. and follow the first tcp packet

![wireshark follow tcp]()

second window will apper and show the tcp packet stream 0.

![tcp packet 0]()

Change the stram 0 to 1 (bottom right side of the window) and here we see the reverse shell is uploading packets.

![tcp packet 1]()

now change 1 to 2 and we can see, this packet run the revres shell

![tcp packet 2]()

now change stream 2 to 3 and we can see, web shell communication.

![tcp packet 3 james passwod and shadow file]()

here we got some some james password and shadow file and much more.

copy the hash file and save into own system crack those passwords. using john tool and fasttrack dicnory (As mention in Question). here is link for [fasttrack dicnory]("https://github.com/trustedsec/social-engineer-toolkit/blob/master/src/fasttrack/wordlist.txt")

`john hash.txt --format=sha512crypt --wordlist=fasttrack.txt`

![shadow file cracked]()

Now once agin deep dive into packet stream 3 and here we can someone try to upload the backdoor. lets open the github link and analysis the code.

![github files]()

This files **main** file look intersting.

![default hash on github]()

after the analysis the code we got lport, lhost, default hash and hash salt.

![salt on github]()

Now lets see tcp stram file in wireshark and here can see attacker use another hash. one more important thing here public key also avlable. save this id_ras key for later use.

![backdoor public key and hash]()

![id rsa key]()

lets crack this hash with salt using **hashcat tool**. make one file name **backdoorhashwithsalt.txt** and put hash and salt in this format **hash:salt**

`hashcat -a 0 -m 1710 backdoorhashwithsalt.txt rockyou.txt`

![backdoor hash cracked]()

after the analysis we have id_ras public key, backdoor password and backdoor port. so lets access the backdoor.

## Backdoor Access

Before the use the id_rsa public key, make sure add the permission to executable.

`ssh -i id_rsa 10.10.84.190 -p 2222`

![user flag]()

We successful login and we got our first user flag.

Here we can see one **suid** permission set so lets run this file.

`./.suid_bash -p`

![root flag]()

Here we got the root flag.

But wait still did not get one answare, lets open the ip into browser we got the last answare there.

![port 80 web page]()

THE END!!!:)