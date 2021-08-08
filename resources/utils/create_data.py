import random
from time import time
from resources.test_data.get_data import feta_data


def generate_string(length: int, digits: bool = False, letters_basic: bool = False, letters_extended: bool = False,
                    symbols_basic: bool = False, symbols_extended: bool = False, blacklisted: bool = False,
                    name_string: bool = False, login_string: bool = False, password_string: bool = False) -> str:
    """Return a string of characters picked from whitelisted_characters in data.yaml according to selected parameters

    :param length:              Integer, representing the length of the returned string
    :param digits:              Boolean, flag indicating if digits should be included in the returned string
    :param letters_basic:       Boolean, flag indicating if basic letters should be included in the returned string
    :param letters_extended:    Boolean, flag indicating if extended letters should be included in the returned string
    :param symbols_basic:       Boolean, flag indicating if basic symbols should be included in the returned string
    :param symbols_extended:    Boolean, flag indicating if extended symbols should be included in the returned string
    :param blacklisted:         Boolean, flag indicating if blacklisted chars should be included in the returned string

    :param name_string:         Boolean, flag indicating if the returned string should consist of allowed name chars
    :param login_string:        Boolean, flag indicating if the returned string should consist of allowed login chars
    :param password_string:     Boolean, flag indicating if the returned string should consist of allowed password chars

    :return:                    String of characters generated according to selected parameters

    Usage examples:
        digits_string = generate_string(50, digits=True)
        letters_string = generate_string(50, letters_basic=True)
        alphanumeric_string = generate_string(50, digits=True, letters_basic=True)
        name_string = generate_string(50, name_string=True)
        login_string = generate_string(50, login_string=True)
        password_string = generate_string(50, password_string=True)
        blacklisted_string = generate_string(50, blacklisted=True)
    """
    result_string = ""
    chars_list = []
    chars = feta_data['whitelisted_characters']
    name_chars = chars['letters_basic'] + chars['letters_extended'] + chars['symbols_basic']
    login_chars = chars['digits'] + chars['letters_basic']
    password_chars = chars['digits'] + chars['letters_basic'] + chars['letters_extended'] + chars['symbols_extended']

    chars_list += chars['digits'] if digits else []
    chars_list += chars['letters_basic'] if letters_basic else []
    chars_list += chars['letters_extended'] if letters_extended else []
    chars_list += chars['symbols_basic'] if symbols_basic else []
    chars_list += chars['symbols_extended'] if symbols_extended else []
    chars_list += chars['blacklisted'] if blacklisted else []

    chars_list += name_chars if name_string else []
    chars_list += login_chars if login_string else []
    chars_list += password_chars if password_string else []

    if not chars_list:
        raise ValueError(f"Please select at least 1 type of characters to generate from")
    for char in range(length):
        test_char = random.choice(chars_list)
        result_string += test_char
    return result_string


def generate_customer(customer_template):
    timestamp = str(int(time()))
    test_customer = customer_template
    test_customer['email'] = test_customer['email'].replace('{placeholder}', timestamp)
    test_customer['password'] = test_customer['password'].replace('{placeholder}', timestamp)
    return test_customer
