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
    """
    Sends a digit string to the server and gets a response string of words
    separated by commas, i.e.: "word,words,more,words"
    """
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (MSG_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)
    response = client.recv(MSG_SIZE).decode(FORMAT)
    print('Server Response:', response)
    return response


def get_words(num):
    """
    Takes a number of words to get from the word generator and calls the send
    function to send it to the socket server.

    When the word string is returned, splits the string at the commas.

    Returns the list of words back to the calling script
    """
    word_str = send(str(num))

    # If last character of word str is a comma, slice it off
    if word_str[-1] == ',':
        word_str = word_str[:-1]

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
