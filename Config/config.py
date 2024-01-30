import time
from mimesis import Person
from mimesis import Gender
from mimesis import Text
import random
import string as s


class TestData:
    BASE_URL = "https://tikitop.io/"
    USER_NAME = "bobbyngayer@gmail.com"
    PASSWORD = "qwertyasd"

    HOME_PAGE_TITLE = "Home | TikiTop"
    PRICING_PAGE_TITLE = "Pricing | TikiTop"
    FAQ_PAGE_TITLE = "FAQ | TikiTop"
    CONTACT_US_PAGE_TITLE = "Contact us | TikiTop"
    PROFILE_PAGE_TITLE = "Account | TikiTop"
    CHANGE_PASSWORD_PAGE_TITLE = "Change Password | TikiTop"
    MAX_CHARACTER_FIRST_NAME_FIELD = 15
    ALL_LETTERS = s.ascii_letters
    UPPERCASE_LETTERS = s.ascii_uppercase
    LOWERCASE_LETTERS = s.ascii_lowercase
    DIGITS = s.digits
    PUNCTUATION = s.punctuation

    @classmethod
    def generate_random_characters(cls, num_char, type_char):
        result = ''
        for i in range(num_char):
            x = random.choice(type_char)
            result += x
        return result

    @classmethod
    def generate_password(cls, num_char, lower, upper, digits):
        password = ''
        for i in range(num_char):
            choose = random.randint(1, 3)
            if choose == 1:
                password += random.choice(lower)
            elif choose == 2:
                password += random.choice(upper)
            elif choose == 3:
                password += random.choice(digits)
        return password

    @classmethod
    def generate_valid_email_address(cls):
        p = Person('en')
        email = p.email()
        return email

    @classmethod
    def generate_first_name(cls):
        p = Person('en')
        first_name = p.first_name()
        return first_name

    @classmethod
    def generate_sentences(cls, quantity):
        text = Text('en')
        message = text.text(quantity)
        return message
