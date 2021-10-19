# Git Happens

`nmap -T4 -sC -sV -p 0-1000 10.10.7.64`

Output:

![nmap scan]("")

here we got port 80 open so open up the IP Address on the browser.

![webpage with html inspection]("")

nmap scan gives very useful information about git directory with url link.

![git hidden directory]("")

lets download the hidden directory using wget command.

`wget --mirror -I .git http://10.10.7.64/.git/`

Now open this downloaded folder into the **Git Cola** software.

Software Info.: Git cola is use for open git reposetory, undo the commits and we can see codes.

![actual git repo files]("")

so undo the commit **Commit > Undo Last Commit**, after 5 time commit we get index.html and we can see there is one hash code, username, encrypt algo. are there, so copy the hash and now decrypt the hash using **John Ripper**

![hashpassword after five times undo git]("")

![john ripper output]("")

so lets try this password in to the login page, but we got nothing so once again go to the git cola and undo the commit two times and we got and password in clear text format.

![final password]("")

THE END!!! :)