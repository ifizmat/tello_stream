# -*- encoding: utf-8 -*-
# Test environment: Python 3.6

import socket
import sys
import time

# In direct connection mode, the default IP address of the robot is 192.168.2.1 and the control command port is port 40923.
host = "192.168.10.1"
port = 8889

def main():
    print("Test Tello stream v0.1: OK.")
    address = (host, int(port))

    # Establish a TCP connection with the control command port of the robot.
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Connecting...")
    # Robomaster EP TCP connection
    #s.connect(address)
    # Tello UDP connection
    s.bind(('', port))
    print("Connected!")
    while True:
        # Wait for the user to enter control commands.
        msg = input(">>> please input SDK cmd: ")

        # When the user enters Q or q, exit the current program.
        if msg.upper() == 'Q':
            break

        # Add the ending character.
        # msg += ';'

        # Send control commands to the robot.
        # s.send(msg.encode('utf-8')) # Robomaster EP TCP connection
        # Tello UDP connection
        s.sendto(msg.encode('utf-8'), address)
        print(f'Sending to {host} command: {msg}')
        time.sleep(1)
        print("Wait 1 second.")
        
        try:
            # Wait for the robot to return the execution result.
            # buf = s.recv(1024) # Robomaster EP TCP connection
            # Tello UDP connection
            buf, ip = s.recvfrom(1024)

            print(f"From {ip}: {buf.decode('utf-8')}")
        except socket.error as e:
            print("Error receiving :", e)
            sys.exit(1)
        if not len(buf):
            break        
    
    # Disconnect the port connection.
    s.shutdown(socket.SHUT_WR)
    s.close()

if __name__ == '__main__':
    main()