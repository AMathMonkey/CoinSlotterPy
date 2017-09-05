'''
Created on Sep 4, 2017

@author: amath
'''

from enum import Enum
from decimal import Decimal, ROUND_HALF_UP

cents = Decimal('0.01')


def get_int(string):
    if string == "":
        return 0
    return int(string)


def format_100cents(float_to_format):
    return Decimal(float_to_format).quantize(cents, ROUND_HALF_UP)


def return_files(country, cbb):
    files = []
    if country == Countries.CANADA:
        if cbb == CBB.COINS or cbb == CBB.COINS_AND_BILLS:
            files.append(open("resources/CADc.txt"))
        if cbb == CBB.BILLS or cbb == CBB.COINS_AND_BILLS:
            files.append(open("resources/CADb.txt"))


    elif country == Countries.SINGAPORE:
        if cbb == CBB.COINS or CBB.COINS_AND_BILLS:
            files.append(open("resources/SGDc.txt"))
        if cbb == CBB.BILLS or CBB.COINS_AND_BILLS:
            files.append(open("resources/SGDb.txt"))

    return files


class Countries(Enum):
    CANADA = 0
    SINGAPORE = 1


class CBB(Enum):
    COINS = 0
    BILLS = 1
    COINS_AND_BILLS = 2


country_map = {
    "Canada/USA": Countries.CANADA,
    "Singapore": Countries.SINGAPORE
}

cbb_map = {
    "Coins": CBB.COINS,
    "Bills": CBB.BILLS,
    "Coins and Bills": CBB.COINS_AND_BILLS
}

inv_country_map = dict((country_map[k], k) for k in country_map)
inv_cbb_map = dict((cbb_map[k], k) for k in cbb_map)


def is_numeric(string):
    try:
        i = int(string)
        return True
    except ValueError:
        return False


global_country = None
global_cbb = None
global_country_string = None
global_cbb_string = None
