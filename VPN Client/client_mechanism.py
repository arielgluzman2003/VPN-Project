import threading
import VPNClient
import multiprocessing
from socket import error as socket_error
import sys

'''
Author: Arie Gluzman
Creation Date: 20.3.2021

*_status_flag* values: 0 - standard, 1 - user stop command, 2 - socket error

class ClientMechanism():
    responsible for creating two processes which communicate with the system and the server,
    also creates a mutual space variable which tells processes to stop.
'''

STANDARD = 0
USER_STOP = 1
SOCKET_ERROR = 2

STOP_MESSAGE = VPNClient.STOP_MESSAGE


class ClientMechanism(multiprocessing.Process):

    def __init__(self, client):
        multiprocessing.Process.__init__(self)
        self._client = client
        self._status_flag = multiprocessing.Value('B', 0)  # one unsigned byte, existing in the shared space
        self._status_flag_lock = multiprocessing.Lock()
        self.client_process = None
        self.thdp_process = None

    def thirdparty_packet(self):  # responsible for reading packet from server and writing to TUN device
        if not self.get_status_flag_value() == USER_STOP:
            thdp = self._client.read_server()
            self._client.write_tun(thdp)

    def client_packet(self):  # responsible for reading packet from TUN device and writing to server
        if not self.get_status_flag_value() == USER_STOP:
            client_pack = self._client.read_tun()
            self._client.write_server(client_pack)
        else:
            self._client.write_server(STOP_MESSAGE)
            print('sent stop message')

    def thirdparty_packet_thread(self, status_flag):  # loop, creating Thread of thirdparty_packet()
        bp = True  # breakpoint
        while bp:
            print(self.get_status_flag_value())
            t = threading.Thread(target=self.thirdparty_packet)
            t.start()
            t.join()
            if self.get_status_flag_value() == USER_STOP:
                bp = False

    def client_packet_thread(self, status_flag):  # loop, creating Thread of client_packet()
        bp = True  # breakpoint
        while bp:
            c = threading.Thread(target=self.client_packet)
            c.start()
            c.join()
            print(self.get_status_flag_value())
            if self.get_status_flag_value() == USER_STOP:
                bp = False
                print('set breakpoint to false')

    def run(self) -> None:  # creates independent processes of client_packet_thread() and thirdparty_packet_thread()
        self.client_process = multiprocessing.Process(target=self.client_packet_thread, args=(self._status_flag,))
        self.thdp_process = multiprocessing.Process(target=self.thirdparty_packet_thread, args=(self._status_flag,))
        self.client_process.start()
        self.thdp_process.start()

    def stop(self):  # changes _status_flag's value to stop
        self.change_status_flag_value(USER_STOP)
        print('stopped, status flag - ', self.get_status_flag_value())

    def change_status_flag_value(self, value):
        '''
        :param value: Integer, new value for _status_flag
        :return: None
        safely changes value of _status_flag, "Locking" use of others until value has been changed.
        '''
        self._status_flag_lock.acquire()
        self._status_flag.value = value
        self._status_flag_lock.release()

    def get_status_flag_value(self):
        '''
        :return: Integer, value of _status_flag
        safely acquires value of _status_flag, "Locking" use of others until value has been acquired.
        '''
        value = 0
        self._status_flag_lock.acquire()
        value = self._status_flag.value
        self._status_flag_lock.release()
        return value
