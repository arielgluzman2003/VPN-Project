'''
Author: Arie Gluzman
Creation Date: 25.3.2021

class CliendHandleMechanism():
    responsible for communication with destination 'host H' and client,
    and for distribution of work between processes and threads for it's purpose.
'''

import threading
import multiprocessing

STOP_MESSAGE = 'STOP'.encode()


class ClientHandleMechanism(multiprocessing.Process):

    def __init__(self, client_handler):
        multiprocessing.Process.__init__(self)
        self._client_handler = client_handler

    def client_packet_thread(self):  # creates loop, thread for client_packet()
        while True:
            c = threading.Thread(target=self.client_packet)
            c.start()
            c.join()

    def thirdparty_packet(self):  # creates loop, thread for thirdparty_packet_thread()
        while True:
            t = threading.Thread(target=self.thirdparty_packet_thread)
            t.start()
            t.join()

    def client_packet(self):  # reads packet from client, writes to TUN device
        client_pack = self._client_handler.read_client()
        if client_pack == STOP_MESSAGE:
            print('CLIENT HINTED STOP')
        else:
            self._client_handler.write_tun(client_pack)

    def thirdparty_packet_thread(self):  # reads packet from TUN device, writes to client
        thdp_packet = self._client_handler.read_tun()
        self._client_handler.write_client(thdp_packet)

    def run(self) -> None:
        c = multiprocessing.Process(target=self.client_packet_thread)
        t = multiprocessing.Process(target=self.thirdparty_packet_thread)
        c.start()
        t.start()