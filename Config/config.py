import time
from mimesis import Person
from mimesis import Gender
from mimesis import Text


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
    


