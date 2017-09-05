"""
Created on Sep 4, 2017

@author: amath
"""

from decimal import Decimal, ROUND_HALF_UP

cents = Decimal('0.01')


# example line for rounding
# Decimal('1.995').quantize(cents, ROUND_HALF_UP)


class CoinSlot(object):
    """
    A class designed to hold a certain number of a single type of coin or bill
    """

    def __init__(self, value, is_coin):
        """
        Constructor for CoinSlot

        :param value: the value of the type of coin that fits in the slot
        :param is_coin: does the slot hold coins (True) or bills (False)?
        """
        if value <= 0:
            raise ValueError("{} is not a valid coin denomination".format(value))

        self.value = value
        self._num_coins = 0
        self.is_coin = is_coin

    def add_coin(self):
        """Add a single coin to the slot"""

        self._num_coins += 1

    def remove_coin(self):
        """Remove a coin from the slot if there is one to remove"""

        if self._num_coins > 0:
            self._num_coins -= 1

    @property
    def num_coins(self):
        """
        Getter for number of coins in slot
        :return: number of coins in slot
        """

        return self._num_coins

    @num_coins.setter
    def num_coins(self, num_coins):
        """
        Setter for number of coins in slot
        :param num_coins: the new number of coins to hold
        :raises ValueError if the number is negative
        """

        if num_coins < 0:
            raise ValueError("{} is not a valid number of coins".format(num_coins))

        self._num_coins = int(num_coins)

    def get_total(self):
        """
        Calculates the value of the coins in the slot
        :return: a value to two decimal places representing the value of the money in the slot
        """
        return Decimal(self.value * self._num_coins).quantize(cents, ROUND_HALF_UP)

    def __str__(self):

        return "CoinSlot holding " + str(self._num_coins) + " " + str(self.value) \
               + " " + "coins" if self.is_coin else "bills" + " with a total value of " + self.get_total()
