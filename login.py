import csv
import sys
from hashing import hash_pass


def login(file_name):
    """
    :param file_name: users information file
    :return: user can login for shopping (customers) or managing the store (admins)
    """
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        users = {}
        for row in reader:
            users[row[1]] = row[2]
    while True:
        username = input('username:')
        if username in users:
            counter = 0
            while counter < 3:
                password = input('password: ')
                if users[username] == hash_pass(password):
                    print('user login done.')
                    break
                else:
                    print('password was wrong. please enter a correct password.')
                    counter += 1
            if counter < 2:
                break
        else:
            print('username is wrong. please enter correct one.')





