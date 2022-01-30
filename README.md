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
