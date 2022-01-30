import VPNServer
import VPNClientHandler
import server_mechanism


def main():
    server = VPNServer.VPNServer()
    while True:
        client = server.accept()
        m = server_mechanism.ClientHandleMechanism(client)
        m.start()


if __name__ == '__main__':
    main()
