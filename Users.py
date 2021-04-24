import csv
from os import path
from pathlib import Path
from hashing import hash_pass


class Users:
    def __init__(self, access_level, username, password, name, phone_number):
        """
        :param access_level: user's access level : admin or customer
        :param username: user's username
        :param password: user's password
        :param name: user's name
        :param phone_number: user's phone number
        """
        self.access_level = access_level
        self.username = username
        self.name = name
        self.phone_number = phone_number
        self.password = password

    @classmethod
    def set_object(cls):
        """
        :return: user's information taken from user and create a class instance.
        """
        acc_level = input('admin | customer :')
        f_name = input('first name:')
        l_name = input('last name:')
        name = f_name + ' ' + l_name
        username = input('select a username:')
        while True:
            pass_1 = input('password:')
            pass_2 = input('confirm your password:')
            if pass_1 == pass_2:
                password = pass_1
                break
            else:
                print('please enter your password again.')
        phone_no = int(input('your phone number:'))

        return cls(acc_level, username, password, name, phone_no)

    def create_account(self):
        """
        :return: create an account for each user and save this information in two separate files:
                                Admin_info_2.csv for admins and Customer_info_2.csv for customers.
        """
        if self.access_level == 'admin':
            with open('Admin_info_2.csv', 'a', newline='') as f:
                fields_name = ['name', 'username', 'password']
                csv_writer = csv.DictWriter(f, fieldnames=fields_name)
                if Path('Admin_info_2.csv').stat().st_size == 0:
                    csv_writer.writeheader()
                csv_writer.writerow({'name': self.name,
                                     'username': self.username,
                                     'password': hash_pass(self.password)})

        elif self.access_level == 'customer':
            with open('Customer_info_2.csv', 'a', newline='') as f:
                fields_name = ['name', 'username', 'password', 'phone_number']
                csv_writer = csv.DictWriter(f, fieldnames=fields_name)
                if Path('Customer_info_2.csv').stat().st_size == 0:
                    csv_writer.writeheader()
                csv_writer.writerow({'name': self.name, 'username': self.username,
                                     'password': hash_pass(self.password), 'phone_number': self.phone_number})

    def shopping(self):
        """
        :return: The list of goods is displayed to the customer using the "display" function.
                The customer begins to choose.
                Until the end of the ordering operation,
                each time the product row number along with the desired number is received from the user
                and stored in a file in the name of customer.
        """

        return 'The list of goods is displayed to the customer using the "display" function.' \
               ' The customer begins to choose. ' \
               'Until the end of the ordering operation, ' \
               'each time the product row number along with the desired number is received from the user ' \
               'and stored in a file in the name of customer.'
