# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/28/2022
# Description:
#
# -----------------------------------------------------------------------------

import socket

MSG_SIZE = 64
PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def send(msg):
    """Does This"""
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (MSG_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)
    response = client.recv(2048).decode(FORMAT)
    print('Server Response:', response)
    return response


def get_words(num):
    """Does this"""

    # Calls send message function to get a string of words separated by commas
    word_str = send(str(num))

    # If last character of word str is a comma, slice it off
    if word_str[-1] == ',':
        word_str = word_str[:-1]

    # Splits word string at commas and puts separated strings in words list
    words = word_str.split(' ')
    print('word list:', words)
    return words


def close_word_gen_server_conn():
    """Sends the server a disconnect message to close the connection"""
    send(DISCONNECT_MESSAGE)


if __name__ == '__main__':
    res = get_words(5)
    print('result =', res)
    send(DISCONNECT_MESSAGE)
