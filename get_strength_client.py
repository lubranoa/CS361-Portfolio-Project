# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/28/2022
# Description:
#
# -----------------------------------------------------------------------------

import socket

MSG_SIZE = 1024
PORT = 12345
HOST = socket.gethostbyname(socket.gethostname())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def get_strength(password):
    """Does this"""

    stren_score_strs = {'0': '0 - Too Guessable: Very Risky Password',
                        '1': '1 - Very Guessable: Risky Password',
                        '2': '2 - Somewhat Guessable: Okay Password',
                        '3': '3 - Safely Unguessable: Good Password',
                        '4': '4 - Very Unguessable: Great Password'}

    client.send(password.encode())

    strength_score = client.recv(MSG_SIZE).decode()
    time_to_crack = client.recv(MSG_SIZE).decode()

    return [stren_score_strs[strength_score], time_to_crack]


def close_strength_client():
    """Does thsis"""
    client.close()


if __name__ == '__main__':
    res = get_strength('correcthorsebatterystaple')
    print('result =', res)
