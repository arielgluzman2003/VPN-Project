'''

Author: Arie Gluzman
Creation Date: 22.3.2021

class VPNServer():
    encapsulation of use of rsa_server.secureServer() and VPNClientHandler.VPNClientHandler()

'''

import tuntap
import rsa_server
import rsa_client
import VPNClientHandler

# CONSTANTS #
DEFAULT_HOST_IP = '0.0.0.0'
DEFAULT_PORT = 1111
SERVER_INFO = (DEFAULT_HOST_IP, DEFAULT_PORT)
MAX_CLIENTS_WAITING = 1
# END #

class VPNServer:

    def __init__(self):
        self._socket = rsa_server.secureServer()
        self._socket.bind(SERVER_INFO)
        self._socket.listen(MAX_CLIENTS_WAITING)
        self._available_octet = 1  # the ending octet of a subnet given to the TUN device value between 1-255
                                   # e.g, '1.1.1.1' then '1.1.1.2' ..... '1.1.1.255'

    def accept(self):  # returns a client handler with the secure socket and available address for TUN device
        self._available_octet += 1  # use of an address
        print('10.0.8.'+str(self._available_octet))
        return VPNClientHandler.VPNClientHandler(self._socket.accept(), str(self._available_octet - 1))
