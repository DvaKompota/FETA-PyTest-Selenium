import pytest
from resources.test_data.get_data import feta_data
from resources.utils.create_data import generate_string


@pytest.mark.create_data
class TestCreateData:

    def test_generate_string(self):
        # Getting all the character collections
        test_string_length = 1000
        digits = feta_data['whitelisted_characters']['digits']
        letters_basic = feta_data['whitelisted_characters']['letters_basic']
        letters_extended = feta_data['whitelisted_characters']['letters_extended']
        symbols_basic = feta_data['whitelisted_characters']['symbols_basic']
        symbols_extended = feta_data['whitelisted_characters']['symbols_extended']
        blacklisted = feta_data['whitelisted_characters']['blacklisted']
        # Validating generation of a string of digits
        digits_string = generate_string(test_string_length, digits=True)
        assert type(digits_string) is str
        assert len(digits_string) == test_string_length
        for char in digits_string:
            assert char in digits
            assert char not in letters_basic + letters_extended + symbols_basic + symbols_extended + blacklisted
        # Validating generation of a string of letters
        letters_string = generate_string(test_string_length, letters_basic=True)
        assert type(letters_string) is str
        assert len(letters_string) == test_string_length
        for char in letters_string:
            assert char in letters_basic
            assert char not in digits + letters_extended + symbols_basic + symbols_extended + blacklisted
        # Validating generation of an alphanumeric string
        alphanumeric_string = generate_string(test_string_length, digits=True, letters_basic=True)
        assert type(alphanumeric_string) is str
        assert len(alphanumeric_string) == test_string_length
        for char in alphanumeric_string:
            assert char in letters_basic + digits
            assert char not in letters_extended + symbols_basic + symbols_extended + blacklisted
        # Validating generation of a name string
        name_string = generate_string(test_string_length, name_string=True)
        assert type(name_string) is str
        assert len(name_string) == test_string_length
        for char in name_string:
            assert char in letters_basic + letters_extended + symbols_basic
            assert char not in digits + symbols_extended + blacklisted
        # Validating generation of a login string
        login_string = generate_string(test_string_length, login_string=True)
        assert type(login_string) is str
        assert len(login_string) == test_string_length
        for char in login_string:
            assert char in digits + letters_basic
            assert char not in letters_extended + symbols_basic + symbols_extended + blacklisted
        # Validating generation of a password string
        password_string = generate_string(test_string_length, password_string=True)
        assert type(password_string) is str
        assert len(password_string) == test_string_length
        for char in password_string:
            assert char in digits + letters_basic + letters_extended + symbols_basic + symbols_extended
            assert char not in blacklisted
        # Validating generation of a string of blacklisted characters
        blacklisted_string = generate_string(test_string_length, blacklisted=True)
        assert type(blacklisted_string) is str
        assert len(blacklisted_string) == test_string_length
        for char in blacklisted_string:
            assert char in blacklisted
            assert char not in digits + letters_basic + letters_extended + symbols_basic + symbols_extended
        # Validating generation of a string with 0 length
        empty_string = generate_string(0, digits=True)
        assert type(empty_string) is str
        assert len(empty_string) == 0
        assert empty_string == ''
        # Validating generation of a string with no parameters raises a ValueError exception
        with pytest.raises(ValueError, match="Please select at least 1 type of characters to generate from"):
            generate_string(test_string_length)
