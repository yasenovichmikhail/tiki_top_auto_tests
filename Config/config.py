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


class HomeTestData:
    HOME_PAGE_TITLE = "Home | TikiTop"
    MAKE_AN_ORDER_BUTTON = "Make an order"
    HOW_IT_WORKS_BUTTON = "How it works?"
    BOOST_YOUR_TIKTOK_PROFILE_HEADER = "BOOST YOUR TIKTOK PROFILE & VIDEOS"
    BOOST_YOUR_TIKTOK_PROFILE_DESCRIPTION = "Promote your new video to get it into people's recommendations. " \
                                            "Buy a subscription to keep your stats up to date. Become popular!"
    WHAT_DO_WE_OFFER_HEADER = "WHAT DO WE OFFER?"

    WHAT_DO_WE_OFFER_GET_MORE_INFO_BUTTON =

    WHAT_WE_HAVE_ALREADY_DONE_HEADER = "WHAT WE'VE ALREADY DONE"

    PROMOTION_FORMATS_HEADER = "PROMOTION FORMATS"

    OUR_CLIENTS_TRUST_US_HEADER = "OUR CLIENTS TRUST US"

    ANY_QUESTIONS_HEADER = "ANY QUESTIONS?"
    ANY_QUESTIONS_DESCRIPTION = "Our services offer high-end promotion packages whose destiny is to power-up your " \
                                "TikTok presence. Boost to the element of your choice immediately —be it likes, " \
                                "views, and whatnot."
    ANY_QUESTIONS_MORE_INFO_BUTTON = "More info"

class PricingTestData:
    PRICING_PAGE_TITLE = "Pricing | TikiTop"


class FaqTestData:
    FAQ_PAGE_TITLE = "FAQ | TikiTop"
    POPULAR_QUESTIONS_HEADER = "POPULAR QUESTIONS"
    FIRST_QUESTION_HEADER = "Is it safe to promote from you?"
    FIRST_QUESTION_DESCRIPTION = "Yap! We only request your username or the link to your TikTok profile." \
                                 " It is enough to boost your TikTok stats. We don't need your password," \
                                 " mail or anything else."
    SECOND_QUESTION_HEADER = "What are the promotion limits?"
    SECOND_QUESTION_DESCRIPTION = "The limit is the maximum number on the Pricing page." \
                                  " This is due to our capacity, we strive to make the limit higher."
    THIRD_QUESTION_HEADER = "What are the accepted payment methods?"
    THIRD_QUESTION_DESCRIPTION = "Now you can pay with credit/debit card through Stripe only. However," \
                                 " we are working on having multiple payment methods for later on."
    FOURTH_QUESTION_HEADER = "Can I promote someone else's account?"
    FOURTH_QUESTION_DESCRIPTION = "Yes, you need only a username or the link to someone else’s account."
    FIFTH_QUESTION_HEADER = "What is Order?"
    FIFTH_QUESTION_DESCRIPTION = "Order is promotion of one category per post."
    SIXTH_QUESTION_HEADER = "What number of days is better to choose for an order?"
    SIXTH_QUESTION_DESCRIPTION = "The more days you choose, the bigger chance that we can boost your" \
                                 " account evenly so as not to arouse suspicion for TikTok. Otherwise," \
                                 " your account can be banned or suspended by TikTok."
    SEVENTH_QUESTION_HEADER = "How to stop an active order?"
    SEVENTH_QUESTION_DESCRIPTION = "If you want to stop an active order, you can delete it but you " \
                                   "should know that your money won't be refunded. Steps to delete an " \
                                   "order: My Profile ➝ Order ➝ Delete Order."
    EIGHTH_QUESTION_HEADER = "Can I do multiple orders on 1 post?"
    EIGHTH_QUESTION_DESCRIPTION = "Yes, you can, but you have to do it with different categories."


class ContactUsTestData:
    CONTACT_US_PAGE_TITLE = "Contact us | TikiTop"
    GET_IN_TOUCH_HEADER = "GET IN TOUCH"
    GET_IN_TOUCH_DESCRIPTION = "Have any questions? We'd love to hear from you"
    FIRST_NAME_TEXT_FIELD_HEADER = "First name"
    FIRST_NAME_FIELD_PLACEHOLDER = "Ex: Paul, Kate, John"
    EMAIL_ADDRESS_TEXT_FIELD_HEADER = "Email address"
    EMAIL_ADDRESS_FIELD_PLACEHOLDER = "tikitop.team@gmail.com"
    MESSAGE_TEXT_AREA_HEADER = "Message"
    MESSAGE_TEXT_AREA_PLACEHOLDER = "Hello! I would like to ask you about..."
    SEND_MESSAGE_BUTTON = "Send message"
    PRIVACY_POLICY_BUTTON = "Privacy Policy"
    PRIVACY_POLICY_HEADER = "PRIVACY POLICY"
    EMAIL_ADDRESS_FIELD_REQUIRED_WARNING = "Required"
    MESSAGE_FIELD_REQUIRED_WARNING = "Required"
    MAX_LENGTH_FIRST_NAME_FIELD_WARNING = "Must be 15 characters or less"
    SUCCESS_SEND_MESSAGE_TEXT = "Your message has been sended"


class ProfileTestData:
    PROFILE_PAGE_TITLE = "Account | TikiTop"