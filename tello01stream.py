# -*- encoding: utf-8 -*-
# Test environment: Python 3.6

import socket
import sys

# In direct connection mode, the default IP address of the robot is 192.168.2.1 and the control command port is port 40923.
host = "192.168.10.1"
port = 8889
print("Test Tello stream v0.1: OK.")

def main():
        address = (host, int(port))

        # Establish a TCP connection with the control command port of the robot.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print("Connecting...")
        s.connect(address)
        print("Connected!")
        # Disconnect the port connection.
        s.shutdown(socket.SHUT_WR)
        s.close()

if __name__ == '__main__':
        main()