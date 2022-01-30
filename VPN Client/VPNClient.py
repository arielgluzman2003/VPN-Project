'''
Author: Arie Gluzman
Creation Date: 20.3.2021

'''

import tuntap
import rsa_client
from routing import set_route

# CONSTANTS #
DEFAULT_MTU = 1500  # bytes ( MTU - Maximum Transmission Unit ) #https://en.wikipedia.org/wiki/Maximum_transmission_unit
STOP_MESSAGE = 'STOP'.encode()


# END #

class VPNClient:

    def __init__(self):
        self._socket = rsa_client.secureClient()
        self._tun_dev = tuntap.device(tuntap.IFF_NO_PI | tuntap.IFF_TUN, b'tun_dev%d')  # new TUN device
        self._tun_dev.configure('10.0.8.0', 24)  # setting addresses related to 10.0.8.0-255

    def connect(self, serverinfo):
        self._socket.connect(serverinfo)

    def read_server(self):
        return self._socket.recv()

    def write_server(self, data):
        self._socket.send(data)

    def read_tun(self):
        return self._tun_dev.read(DEFAULT_MTU)

    def write_tun(self, data):
        return self._tun_dev.write(data)

    def onset_routing(self):  # changing default routing table
        set_route(operation=True, subnet='default', netmask='0', gateway=self._tun_dev.subnet,
                  device=self._tun_dev.name)
        set_route(operation=False, subnet='default', netmask='0', gateway='192.168.1.1', device='enp0s3')
        set_route(operation=True, subnet='192.168.1.223', netmask='32', gateway='192.168.1.1', device='enp0s3')

    def termination_routing(self):  # reverting routing table to default
        set_route(operation=False, subnet='default', netmask='0', gateway=self._tun_dev.subnet,
                  device=self._tun_dev.name)
        set_route(operation=True, subnet='default', netmask='0', gateway='192.168.1.1', device='enp0s3')
        set_route(operation=False, subnet='192.168.1.223', netmask='32', gateway='192.168.1.1', device='enp0s3')
        self._tun_dev.deconfigure()
        self._tun_dev.terminate()
