import socket
import json

def udp_echo_client(server_host='localhost', server_port=7000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (server_host, server_port)

    try:
        while True:
            message = input()
            message = {
                'command': 'connect',
                'username': 'ionic101'
            }
            print('send', json.dumps(message).encode())

            sent = sock.sendto(json.dumps(message).encode(), server_address)

    finally:
        print('Closing socket')
        sock.close()

if __name__ == "__main__":
    udp_echo_client()
