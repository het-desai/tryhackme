# Kerberos

## What's Kerberos?

- Kerberos is the default authentication service for Microsoft Windows domains.

- It is intended to be more "secure" than NTLM by using third party ticket authorization as well as stronger encryption.

## Common Terminology

- Ticket Granting Ticket (TGT): A ticket-granting ticket is an authentication ticket used to request service tickets from the TGS for specific resources from the domain.

- Key Distribution Center (KDC): The Key Distribution Center is a service for issuing TGTs and service tickets that consist of the Authentication Service and the Ticket Granting Service.

- Authentication Service (AS): The Authentication Service issues TGTs to be used by the TGS in the domain to request access to other machines and service tickets.

- Ticket Granting Service (TGS): The Ticket Granting Service takes the TGT and returns a ticket to a machine on the domain.

- Service Principal Name (SPN): A Service Principal Name is an identifier given to a service instance to associate a service instance with a domain service account. Windows requires that services have a domain service account which is why a service needs an SPN set.

- Privilege Attribute Certificate (PAC): The PAC holds all of the user's relevant information, it is sent along with the TGT to the KDC to be signed by the Target LT Key and the KDC LT Key in order to validate the user.

- KDC Long Term Secret Key (KDC LT Key): The KDC key is based on the KRBTGT service account. It is used to encrypt the TGT and sign the PAC.

- Client Long Term Secret Key (Client LT Key): The client key is based on the computer or service account. It is used to check the encrypted timestamp and encrypt the session key.

- Service Long Term Secret Key (Service LT Key): The service key is based on the service account. It is used to encrypt the service portion of the service ticket and sign the PAC.

- Session Key: Issued by the KDC when a TGT is issued. The user will provide the session key to the KDC along with the TGT when requesting a service ticket.

## AS-REQ Pre-Authentication In Detail

- The AS-REQ step in Kerberos authentication starts when a user requests a TGT from the KDC.

- In order to validate the user and create a TGT for the user, the KDC must follow these exact steps.

- The first step is for the user to encrypt a timestamp NT hash and send it to the AS.

- The KDC attempts to decrypt the timestamp using the NT hash from the user, if successful the KDC will issue a TGT as well as a session key for the user.

## Ticket Granting Ticket Contents

- Ticket Granting Ticket (TGT) encrypted using KDC LT Key

- TGT Contents nine things.

1. Start/End/Max Renew date and time: 5/29/2021 1:39; 5/29/2021 22:39

2. Service Name: krbtgt, example.local

3. Target Name: krbtgt, example.local

4. Client Name: user, example.local

5. Flags: 0000e0000

6. Session Key: 00x00001sfd120

7. Privilege Attribute Certificate:

    - Username: example
    
    - SID: S-0-5-45......

8. Signed w/Service LT Key

9. Signed w/KDC LT Key

## Service Ticket Contents

- A service ticket contains two portions:

1. Service Portion:

    - User Details
    
    - Session Key
    
    - Encrypts the ticket with the service account NTLM hash.

2. User Portion:

    - Validity Timestamp
    
    - Session Key
    
    - Encrypts with the TGT session key.

## Working model of kerberos

[Follow this youtube link]("https://www.youtube.com/watch?v=_44CHD3Vx-0")

## Abusing Pre-Authentication Overview

- By brute-forcing Kerberos pre-authentication, you do not trigger the account failed to log on event which can throw up red flags to blue teams.

- When brute-forcing through Kerberos you can brute-force by only sending a single UDP frame to the KDC allowing you to enumerate the users on the domain from a wordlist.

### Enumerating Users Kerbrute

`kerbrute userenum --dc CONTROLLER.local -d CONTROLLER.local uname.txt`

## Harvesting & Brute-Forcing Tickets Rubeus

### Harvesting Tickets

- Rubeus is a powerful tool for attacking Kerberos.

- Rubeus is tool works when we are present in target machine.

`Rubeus.exe harvest /interval:30`

- This command tells Rebeus to harvest for TGT's every 30 seconds.

### Brute-Forcing Tickets

- There is 2 type of password attack

1. Brute-Force: select one user and test all posible password combination to that particular user

2. Password Spray: select one password and test it on all user accounts.

- This attack will take a given Kerberos-based password and spray it against all found users and give a .kirbi ticket.

- This ticket is a TGT that can be used in order to get service tickets from the KDC as well as to be used in attacks like the pass the ticket attack.

- Note: you need to add the domain controller domain name to the windows host file. follow the command:

`echo MACHINE_IP CONTROLLER.local >> C:\Windows\System32\drivers\etc\hosts`

- Now we can spray the password to user accounts. follow the bellow command:

`Rubeus.exe brute /password:Password1 /noticket`

- This will take a given password and "spray" it against all found users then give the .kirbi TGT for that user.

- Be mindful of how you use this attack as it may lock you out of the network depending on the account lockout policies.

## Kerberosting Rubeus & Impacket

### Kerberoasting Rubeus (Method 1)

- this attack performing within the target machine

`Rubeus.exe kerberoast`

- This will dump the Kerberos hash of any kerberoastable users.

- we can crack the hash using john or hashcat

### Kerberoasting Impacket

- this attack performing in own kali machine and try to teg hashing from target machine.

`GetUserSPNs.py controller.local/Machine1:Password1 -dc-ip 10.10.10.60 -request`

- this will dump the Kerberos hash for all kerberoastable accounts it can find on the target domain just like Rubeus does; however, this does not have to be on the targets machine and can be done remotely.

- after getting hash, now crack that hash using john or hashcat.

### Kerberoasting Mitigation

- Strong Service Passwords - If the service account passwords are strong then kerberoasting will be ineffective

- Don't Make Service Accounts Domain Admins - Service accounts don't need to be domain admins, kerberoasting won't be as effective if you don't make service accounts domain admins.

## AS-REP Roasting Rubeus

### Dumping KRBASREP5 Hashes Rubeus

`Rubeus.exe asreproast`

- This will run the AS-REP roast command looking for vulnerable users and then dump found vulnerable user hashes.

### AS-REP Roasting Mitigations

- Have a strong password policy. With a strong password, the hashes will take longer to crack making this attack less effective

- Don't turn off Kerberos Pre-Authentication unless it's necessary there's almost no other way to completely mitigate this attack other than keeping Pre-Authentication on.

## Pass the Ticket mimikatz

### Dump Tickets

- `mimikatz.exe`: run mimikatz

- `privilege::debug`: Ensure this outputs `[output '20' OK]` if it does not that means you do not have the administrator privileges to properly run mimikatz

- `sekurlsa::tickets /export`: this will export all of the .kirbi tickets into the directory that you are currently in

### Pass the Ticket Mimikatz

- `kerberos::ptt [ticket]`: run this command inside of mimikatz with the ticket that you harvested from earlier. It will cache and impersonate the given ticket

- `klist`: Here were just verifying that we successfully impersonated the ticket by listing our cached tickets. this command need to be run outside the mimikat; like on terminal.

### Pass the Ticket Mitigation

- Don't let your domain admins log onto anything except the domain controller - This is something so simple however a lot of domain admins still log onto low-level computers leaving tickets around that we can use to attack and move laterally with.

## Golden & Silver Ticket

[Golden Ticket and Silver Ticket]("")

## Skeleton Key

### Install the skeleton key in mimikatz

- The Kerberos backdoor works by implanting a skeleton key that abuses the way that the AS-REQ validates encrypted timestamps. A skeleton key only works using Kerberos RC4 encryption. 

- The default hash for a mimikatz skeleton key is 60BA4FCADC466C7A033C178194C03DF6 which makes the password -"mimikatz"

`misc::skeleton`

- skeleton key works like master key of the all user accounts and services.

## Some useful Resource

[Resource 1]("https://posts.specterops.io/kerberoasting-revisited-d434351bd4d1")

[Resource 2: very well explain Golden Ticket and selver ticket and much more]("https://www.varonis.com/blog/kerberos-authentication-explained/")

[Resource 3]("https://www.redsiege.com/wp-content/uploads/2020/04/20200430-kerb101.pdf")
