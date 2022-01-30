'''

Author: Arie Gluzman
Creation Date: Unknown, 2021

class ApplicationFrame():
    responsible for the Graphics User-Interface (GUI), and for the Initiation and Termination of Client Mechanism
'''

import tkinter.messagebox
from tkinter import Frame, Button, Tk, font, Label, messagebox
import VPNClient
import client_mechanism
import sys

# Constants #
DEFAULT_TITLE = 'Welcome!'
MODE_ON_TITLE = 'VPN Turned ON'
MODE_OFF_TITLE = 'VPN Turned OFF'

DEFAULT_BUTTON_TEXT_PADDING_X = 10
DEFAULT_BUTTON_TEXT_PADDING_Y = 10

MODE_ON_BUTTON_TEXT = 'Stop'
MODE_OFF_BUTTON_TEXT = 'Start'

DEFAULT_BUTTON_FONT = None

MODE_ON_BUTTON_BACKGROUND_COLOR = 'red'
MODE_OFF_BUTTON_BACKGROUND_COLOR = 'green'
MODE_ON_BUTTON_FOREGROUND_COLOR = 'white'
MODE_OFF_BUTTON_FOREGROUND_COLOR = 'black'

DEFAULT_SIZE = '300x300'

DEFAULT_SERVER_IP = '192.168.1.223'
DEFAULT_PORT = 1111
SERVER_INFO = (DEFAULT_SERVER_IP, DEFAULT_PORT)


# Constants #

class ApplicationFrame(Frame):

    def __init__(self, master):  # creates all graphical assets, constants, variables and other assets
        self.client = None
        self.m = None
        self.server_ip = '192.168.1.255'
        self.ping = '10'
        self.avg_packets = '10'
        self.total_packets = '500'
        self.master = master
        self.master.protocol('WM_DELETE_WINDOW', self.exit_protocol)
        self.master.geometry(DEFAULT_SIZE)
        self.master.title(DEFAULT_TITLE)
        self.operation_button = Button(master, text=MODE_OFF_BUTTON_TEXT, command=self.operation,
                                       bg=MODE_OFF_BUTTON_BACKGROUND_COLOR, fg=MODE_OFF_BUTTON_FOREGROUND_COLOR,
                                       padx=DEFAULT_BUTTON_TEXT_PADDING_X, pady=DEFAULT_BUTTON_TEXT_PADDING_Y)
        self.operation_button.place(x=65, y=150)  # setting default location for OPERATION button
        self.master.bind('<Control-s>',
                         self.keybind_operation)  # creates a bind for Ctrl+S, as alternative to Operation button
        DEFAULT_BUTTON_FONT = font.Font(family='Helvetica', size=50)
        self.operation_button['font'] = DEFAULT_BUTTON_FONT
        self.server_ip_label = Label(self.master, text='server IP address: ' + self.server_ip)
        self.ping_label = Label(self.master, text='ping: ' + self.ping + 'ms')
        self.avg_packets_label = Label(self.master, text='average packets: ' + self.avg_packets + '\\s')
        self.total_packets_label = Label(self.master, text='total packets: ' + self.total_packets)
        self.server_ip_label.pack()
        self.avg_packets_label.pack()
        self.total_packets_label.pack()
        self.ping_label.pack()
        self.operating = False

    def operation(self):  # function which runs when OPERATION button is pressed, switches self.operating every press
        if self.operating:  # when operation button is pressed and program is running, meaning - STOP
            self.operation_button.configure(text=MODE_OFF_BUTTON_TEXT, bg=MODE_OFF_BUTTON_BACKGROUND_COLOR,
                                            fg=MODE_OFF_BUTTON_FOREGROUND_COLOR)
            self.master.title(MODE_OFF_TITLE)
            self.operating = False
            self.stop_client()
        else:  # when operation button is pressed and program is not running, meaning - START
            self.operation_button.configure(text=MODE_ON_BUTTON_TEXT, bg=MODE_ON_BUTTON_BACKGROUND_COLOR,
                                            fg=MODE_ON_BUTTON_FOREGROUND_COLOR)
            self.master.title(MODE_ON_TITLE)
            self.operating = True
            self.start_client()

    def start_client(self):  # creating all mechanisms relevant, does necessary changes to system
        self.client = VPNClient.VPNClient()
        self.client.onset_routing()
        self.client.connect(SERVER_INFO)
        self.m = client_mechanism.ClientMechanism(self.client)
        self.m.start()

    def stop_client(self):  # shuts down mechanisms, reverts system changes
        self.m.stop()
        self.client.termination_routing()

    def exit_protocol(self):  # responsible for graphics and stopping mechanisms after pressing the exit button
        if tkinter.messagebox.askokcancel('Are you sure you want to exit?',
                                          'By Clicking "OK" You Will Be Disconnected from Service'):
            if self.operating:
                self.stop_client()
                self.operating = False
            self.master.destroy()

    def keybind_operation(self, event):  # runs when key-bind is pressed, alternative to the OPERATION button
        self.operation()
