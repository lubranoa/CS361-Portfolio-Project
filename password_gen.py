# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/16/2022
# Description:
# -----------------------------------------------------------------------------

import random
import string


def generate_password(parameters):

    desired_chars = ''
    password = ''

    if parameters[1] == 1:
        desired_chars = desired_chars+string.ascii_lowercase
    if parameters[2] == 1:
        desired_chars = desired_chars + string.ascii_uppercase
    if parameters[3] == 1:
        desired_chars = desired_chars + string.digits
    if parameters[4] == 1:
        desired_chars = desired_chars + '!@#$%^&*'
    if parameters[5] == 1:
        remove_chars = 'Il1O0'
        for char in remove_chars:
            desired_chars = desired_chars.replace(char, '')

    print(desired_chars)

    while len(password) < parameters[0]:
        new_char = random.choice(desired_chars)
        if parameters[6] == 1 and new_char in password:
            print('duplicate', new_char, 'skipped')
            continue
        password = password + new_char

    print('password length:', len(password))

    return password


def nothing():
    return 'nothing'


if __name__ == '__main__':
    pword_params = [20, 1, 1, 1, 1, 1, 1]
    pword = generate_password(pword_params)
    print(pword)

