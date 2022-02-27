# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/26/2022
# Description: This microservice generates a password for the Password
#     Generator app's GUI by receiving a list of parameters, generating a
#     password that adheres to those parameters, and sending the password back
#     to the GUI.
#
# -----------------------------------------------------------------------------

import random
import string


def generate_password(params: dict):
    """
    Generates a password consisting of a specified number of characters, that
    will adhere to one or more of the following:
        - includes lowercase letters
        - includes uppercase letters
        - includes digits
        - includes a short list of special characters
        - excludes similar characters that could be mistaken for each other
        - excludes duplicate characters
        - include a minimum number of digits
        - include a minimum number of special characters

    Dictionary must contain a password length, a lowercase Bool, an uppercase
    Bool, a digits Bool, a special character Bool, exclude ambiguous Bool,
    exclude duplicates Bool, a minimum number of digits, and a minimum number
    of special characters using these strings as keys:

    'len', 'low_case', 'upp_case', 'digits', 'special', 'no_ambig', 'no_dup',
    'min_dig', 'min_spec'

    Returns a generated password that adheres to the specified criteria
    """

    # TODO: Add functionality for minimum number of digits and minimum number
    #       of special characters

    spec_chars = '!@#$%^&*'
    ambig_chars = 'Il1O0'
    desired_chars = ''
    password_chars = []

    # If "include a-z" selected, picks single random a-z char, add it to
    # password chars list, and concats lower str to desired str
    if params['low_case']:
        lower_chars = string.ascii_lowercase

        # If "no ambiguous chars" selected, removes 'l' from lower str
        if params['no_ambig']:
            lower_chars.replace('l', '')

        mand_char = random.choice(lower_chars)

        # If "no duplicates" selected, removes chosen char from desired str
        if params['no_dup']:
            lower_chars.replace(mand_char, '')

        password_chars.append(mand_char)
        desired_chars = desired_chars + lower_chars

    # If "include A-Z" selected, picks single random A-Z char, add it to
    # password chars list, and concats upper str to desired str
    if params['upp_case']:
        upper_chars = string.ascii_uppercase

        # If user selected "no ambiguous chars", ensures an "I" or an "O" are
        # not chosen for a mandatory uppercase letter
        if params['no_ambig']:
            upper_chars.replace('I', '')
            upper_chars.replace('O', '')

        mand_char = random.choice(string.ascii_uppercase)

        if params['no_dup']:
            upper_chars.replace(mand_char, '')

        password_chars.append(mand_char)
        desired_chars = desired_chars + upper_chars

    # If "include 0-9" selected, picks single random 0-9 char, add it to
    # password chars list, and concats digit str to desired str
    if params['digits']:
        digit_chars = string.digits

        # If "no ambiguous chars" selected, removes "0" and "1" from digit str
        if params['no_ambig']:
            digit_chars.replace('0', '')
            digit_chars.replace('1', '')

        mand_char = random.choice(digit_chars)

        # If "no duplicates" selected, removes chosen digit from digit str
        if params['no_dup']:
            digit_chars.replace(mand_char, '')

        password_chars.append(mand_char)
        desired_chars = desired_chars + digit_chars

    if params['special']:
        mand_char = random.choice(spec_chars)

        if params['no_dup']:
            spec_chars.replace(mand_char, '')

        password_chars.append(mand_char)
        desired_chars = desired_chars + spec_chars

    if params['no_ambig']:
        for char in ambig_chars:
            desired_chars = desired_chars.replace(char, '')

    print(desired_chars)
    desired_chars = random.sample(desired_chars, k=len(desired_chars))

    if params['no_dup']:
        while len(password_chars) < params['len'] and len(desired_chars) > 0:
            new_char = random.choice(desired_chars)
            password_chars.append(new_char)
            desired_chars.remove(new_char)
    else:
        while len(password_chars) < params['len'] and len(desired_chars) > 0:
            new_char = random.choice(desired_chars)
            password_chars.append(new_char)

    random.shuffle(password_chars)
    password = ''.join(password_chars)

    print('password length:', len(password))

    return password


if __name__ == '__main__':
    pword_params = {
        'len': 20,
        'low_case': True,
        'upp_case': True,
        'digits': True,
        'special': True,
        'no_ambig': True,
        'no_dup': True,
        'min_dig': 1,
        'min_spec': 1
    }
    pword = generate_password(pword_params)
    print(pword)
