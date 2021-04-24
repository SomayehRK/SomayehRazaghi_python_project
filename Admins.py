from Users import Users
from Goods import Goods


class Admins(Users):
    def __init__(self, username, name, password):
        """
        :param username: admin's username
        :param name: admin's name
        :param password: admin's password
        """
        super().__init__('admin', username, name, 0, password)

    @staticmethod
    def define_goods():
        """
        :return: Inserts new goods information using the "set_object()" method from the Goods Class.
        """

        return 'Inserts new goods information using the "set_object()" method from the Goods Class.'

    @staticmethod
    def view_invoices():
        """
        :return: admin can view invoices of customers base their date.
        """

        return 'admin can view invoices of customers base their date.'
