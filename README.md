31 January 2022<br />
author: Ariel Gluzman (ariel.gluzman@gmail.com)<br /><br />
# VPN-Project
A VPN Server and Client kit, for user to set-up on computers he wishes to forward, hide, encrypt traffic through,
uses high-standard encryption protocols, and supports multiple clients.

### Requirements
* Unix-Based machine, a user with SUPER-USER (sudo) permissions
* packages [rsa](https://stuvel.eu/software/rsa/), [Pycryptodome](https://www.pycryptodome.org/en/latest/src/introduction.html), [Scapy](https://scapy.net/) installed, see [installation](#installation)


## Installation
Some operations require super-user (`sudo ..`) permissions to run properly,
Python modules installed with super-user permissions are not available when running python as super-user and vice-versa
and thus installation is to be done as super-user
run the following command in a new terminal window (Ctrl+Alt+T):</br>
```
> sudo pip3 install rsa
> sudo pip3 install pycryptodome
> sudo pip3 install scapy
```
when finished, fetch the needed code from this site use:</br>
`> git clone https://github.com/arielgluzman2003/VPN-Project.git`</br></br>
or simply click the **_Code -> Download ZIP_**, and Extract in desired location.
## Setup
#### Server
On one machine from which Server will operate save folder /VPN-Project/VPN Server.</br>
as mentioned before super-user permission is needed to run, use:</br>
<code> $VPN-Project/VPN Server> sudo python3 main.py </code>
#### Client
On other machine(s) from which Client(s) will operate save folder /VPN-Project/VPN Client.</br>
use: 
<code> $VPN-Project/VPN Client> sudo python3 main.py </code></br>
**_START_** to connect and forward encrypted traffic</br>
_**STOP**_ to disconnect and revert network configuration</br>

## Recommended Setup
#### Editing code in IDE
if you wish to run edit & run code from and IDE (PyCharm etc.) you will need extra configurations for your interpreter:</br>
first, create a bash file '_python-sudo.sh_':
  ```
  sudo python3 "$@"
  ```
give it execution permissions: </br>&nbsp;&nbsp;&nbsp;
<code> $> sudo chmod +x python-sudo.sh </code></br>
later you could run scripts as super-user without using _sudo_ explicitly: </br>&nbsp;&nbsp;&nbsp;
<code> $> ./python-sudo.sh script.py </code></br>

add '_python-sudo.sh_' as path for **_new project interpreter_**, scripts shall run as super-user.
#### Make SUDO by default
when running `sudo ..` commands for the first time in a new tab, user is asked to enter password,</br>
and you may run into a problem running '_python-sudo.sh_' as **Project-Interpreter**, because it will not enter your password,</br> a simple configuration is to be done to disable the constant requirement to enter a password:

In Unix System files there is a file '_**/etc/sudoers**_' in which permissions for users to use </br>
super-user permissions without typing sudo and requiring administrator password.</br>
_**it is unsafe**_ to edit file directly, although it is possible: </br>
<code> $> sudo nano /etc/sudoers </code> </br>

there is a tool called _**visudo**_ that helps safely edit '_**/etc/sudoers**_', use:</br>
<code> $> sudo visudo </code> </br>

add the following line at the end of the file (**_user_** stands for your username):</br>
<code> %user ALL=(ALL) NOPASSWD:ALL </code> </br>

Save file.
