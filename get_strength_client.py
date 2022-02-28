# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/28/2022
# Description: GUI file imports this as a module in order to pass my teammate's
#     Password Strength Tester service a password and receive strength and time
#     to crack data from the service. Communicates via Python sockets over a
#     local network. The function in this module returns the strength data back
#     to the GUI file for it to display the strength data to the user. My
#     teammate's service uses Dropbox's "zxcvbn" password strength estimator
#     via their zxcvbn Python package.
#
# -----------------------------------------------------------------------------

import socket

stren_strs = {'0': '0 - Too Guessable: Very Risky Password',
              '1': '1 - Very Guessable: Risky Password',
              '2': '2 - Somewhat Guessable: Okay Password',
              '3': '3 - Safely Unguessable: Good Password',
              '4': '4 - Very Unguessable: Great Password'}
MSG_SIZE = 1024
PORT = 12345
HOST = socket.gethostbyname(socket.gethostname())


def get_strength(password: str):
    """
    Gets password strength data by connecting to an already running socket
    server at the designated port and host, sending the password to the server,
    and catching the two responses. Closes the connection when done. Returns
    the data to the GUI file.

    :param password: a password or passphrase
    :return: list of two strings ['score', 'time to crack']
    """
    # Create a client socket object and connect it to host socket server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Send password to server
    client.send(password.encode())

    # Catch server's two responses
    strength_score = client.recv(MSG_SIZE).decode()
    time_to_crack = client.recv(MSG_SIZE).decode()

    client.close()    # Close client's connection to server

    # Return strength data as a list
    return [stren_strs[strength_score], time_to_crack]


if __name__ == '__main__':
    res = get_strength('correcthorsebatterystaple')
    print('result =', res)
