# coding=utf-8
import socket
import time
import cv2

# Video stream, server socket
VS_UDP_IP = '0.0.0.0'
VS_UDP_PORT = 11111
cap = None
video_address = 'udp://@' + VS_UDP_IP + ':' + str(VS_UDP_PORT)  # + '?overrun_nonfatal=1&fifo_size=5000'



def get_udp_video_address():
    return 'udp://@' + VS_UDP_IP + ':' + str(VS_UDP_PORT)  # + '?overrun_nonfatal=1&fifo_size=5000'

def get_video_capture():
    """Get the VideoCapture object from the camera drone
    Returns:
        VideoCapture
    """
    if cap is None:
        cap = cv2.VideoCapture(get_udp_video_address())

    if not cap.isOpened():
        cap.open(get_udp_video_address())
    return cap

def main():


if __name__ == '__main__':
    main()