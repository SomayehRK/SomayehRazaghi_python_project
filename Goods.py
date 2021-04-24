class Goods:
    def __init__(self, barcode, name, brand, price, stock):
        """
        :param barcode: product's barcode
        :param name: product's name
        :param brand: product's brand
        :param price: product's price
        :param stock: product's stock
        """
        self.barcode = barcode
        self.name = name
        self.brand = brand
        self. price = price
        self.stock = stock

    @staticmethod
    def set_object():
        """
        :return: with this methode information of each item is taken from admin and stored in a file
        """

        return 'with this methode information of each item is taken from admin and stored in a file'

    def __str__(self):
        """
        :return: print product's information in a table
        """
        item_info = [self.barcode, self.name, self.brand, self.price, self.stock]
        return tabulate(item_info, headers=['barcode', 'name', 'brand', 'price', 'stock'])
