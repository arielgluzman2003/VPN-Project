'''

Author: Arie Gluzman
Creation Date: 22.3.2021

class VPNClientHandler():
    a collection of attributes and functions for communication with the client and the external host

'''

import rsa_client
import tuntap


class VPNClientHandler:

    def __init__(self, securesocket, available_octet):
        if type(available_octet) is not str:
            raise ValueError('')
        elif not available_octet.isnumeric():
            raise ValueError('')
        elif not 0 <= int(available_octet) <= 255:
            raise ValueError('Last octet %s is invalid, must be between 0-255' % available_octet)
        self._socket = securesocket
        self._tun_dev = tuntap.device(tuntap.IFF_NO_PI | tuntap.IFF_TUN,
                                      b'tun_dev%d')  # TUN device with the next available name of type 'tun_dev%d'
                                                     # e.g, 'tun_dev0'
        self._tun_dev.configure('10.0.8.' + available_octet, 24)  # configuration of device on the system
        print('DEVICE NAME: ' + self._tun_dev.name)

    def read_client(self):
        return self._socket.recv()

    def write_client(self, data):
        self._socket.send(data)

    def read_tun(self):
        return self._tun_dev.read(1500)

    def write_tun(self, data):
        self._tun_dev.write(data)
