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

    WHAT_DO_WE_OFFER_CONTAINER_HEADER = "WHAT DO WE OFFER?"
    WHAT_DO_WE_OFFER_FOLLOWERS_HEADER = "Followers"
    WHAT_DO_WE_OFFER_FOLLOWERS_DESCRIPTION = "Get active subscribers to your profile"
    WHAT_DO_WE_OFFER_LIKES_HEADER = "Likes"
    WHAT_DO_WE_OFFER_LIKES_DESCRIPTION = "Get likes on any of your videos with a deadline"
    WHAT_DO_WE_OFFER_VIEWS_HEADER = "Views"
    WHAT_DO_WE_OFFER_VIEWS_DESCRIPTION = "Increase the number of views of your posts"
    WHAT_DO_WE_OFFER_COMMENTS_HEADER = "Comments"
    WHAT_DO_WE_OFFER_COMMENTS_DESCRIPTION = 'Get real comments like "Wow!!!" and "xD".'
    WHAT_DO_WE_OFFER_SHARES_HEADER = "Shares"
    WHAT_DO_WE_OFFER_SHARES_DESCRIPTION = "Make promotion more real for algorithms"
    WHAT_DO_WE_OFFER_GET_MORE_INFO_BUTTON = "Get  more info"
    WHAT_DO_WE_OFFER_TIKTOK_PROFILE_BOOSTING_HEADER = "We offer TikTok profile boosting at a fair price"
    WHAT_DO_WE_OFFER_TIKTOK_PROFILE_BOOSTING_DESCRIPTION_1 = "Our services offer high-end promotion packages whose " \
                                                             "destiny is to power-up your TikTok presence. Boost to " \
                                                             "the element of your choice immediately —be it likes, " \
                                                             "views, and whatnot."
    WHAT_DO_WE_OFFER_TIKTOK_PROFILE_BOOSTING_DESCRIPTION_2 = "We have tried to develop a system that best suits the " \
                                                             "requirements of TikTok users. Remember, we are on your " \
                                                             "side! Start today, and see positive results in no time!"

    WHAT_WE_HAVE_DONE_CONTAINER_HEADER = "WHAT WE'VE ALREADY DONE"
    WHAT_WE_HAVE_DONE_ORDERS_HEADER = "137 orders"
    WHAT_WE_HAVE_DONE_ORDERS_DESCRIPTION = "have been placed for the entire time of our service"
    WHAT_WE_HAVE_DONE_LIKES_HEADER = "391K likes"
    WHAT_WE_HAVE_DONE_LIKES_DESCRIPTION = "were clicked under our customers' videos"
    WHAT_WE_HAVE_DONE_FOLLOWERS_HEADER = "27K followers"
    WHAT_WE_HAVE_DONE_FOLLOWERS_DESCRIPTION = "subscribed since the launch of the project"
    WHAT_WE_HAVE_DONE_VIEWS_HEADER = "328K views"
    WHAT_WE_HAVE_DONE_VIEWS_DESCRIPTION = "were received on our users' videos"

    PROMOTION_FORMATS_CONTAINER_HEADER = "PROMOTION FORMATS"
    PROMOTION_FORMATS_SUBSCRIPTION_PLAN_HEADER = "Subscription plan"
    PROMOTION_FORMATS_SUBSCRIPTION_PLAN_DESCRIPTION = "Subscribe for the plan to get consistent activity on your " \
                                                      "profile during the month."
    PROMOTION_FORMATS_STANDARD_ORDERS_HEADER = "Standart orders"
    PROMOTION_FORMATS_STANDARD_ORDERS_DESCRIPTION = "Promote your profile or your specific videos within a selected " \
                                                    "time frame."
    PROMOTION_FORMATS_WANT_LEARN_MORE_HEADER = "Want to learn more?"
    PROMOTION_FORMATS_WANT_LEARN_MORE_DESCRIPTION = "Explore more opportunities to boost your TikTok account!"
    PROMOTION_FORMATS_GET_MORE_INFO_BUTTON = "Get more info"
    PROMOTION_FORMATS_ONE_STORY_HEADER = "The story of one subscription"
    PROMOTION_FORMATS_ONE_STORY_NAME = "Edward"
    PROMOTION_FORMATS_ONE_STORY_REVIEW = "Hi! A couple of months ago I got myself a subscription. I want to share " \
                                         "my experience with you"
    PROMOTION_FORMATS_ONE_STORY_STEP_1_HEADER = "Get the plan"
    PROMOTION_FORMATS_ONE_STORY_STEP_1_DESCRIPTION = "Choose the plan you want and pay monthly"
    PROMOTION_FORMATS_ONE_STORY_STEP_2_HEADER = "Post the video"
    PROMOTION_FORMATS_ONE_STORY_STEP_2_DESCRIPTION = "You must publish at least one video to promote them"
    PROMOTION_FORMATS_ONE_STORY_STEP_3_HEADER = "Get subscribers"
    PROMOTION_FORMATS_ONE_STORY_STEP_3_DESCRIPTION = "People will subscribe to you evenly within a month"
    PROMOTION_FORMATS_ONE_STORY_STEP_4_HEADER = "Get promotion for your videos"
    PROMOTION_FORMATS_ONE_STORY_STEP_4_DESCRIPTION = "Every day we will boost 5 of your latest videos"

    OUR_CLIENTS_TRUST_US_CONTAINER_HEADER = "OUR CLIENTS TRUST US"
    OUR_CLIENTS_TRUST_US_PEACE_OF_MIND_HEADER = "Total Peace of Mind"
    OUR_CLIENTS_TRUST_US_PEACE_OF_MIND_DESCRIPTION = "The whole process is automated. You don't have to do anything " \
                                                     "except post your videos"
    OUR_CLIENTS_TRUST_US_AUTOMATIC_BOOST_HEADER = "Automatic Boost"
    OUR_CLIENTS_TRUST_US_AUTOMATIC_BOOST_DESCRIPTION = "Subscription promotion format automatically promotes all " \
                                                       "your new videos"
    OUR_CLIENTS_TRUST_US_PERSONAL_PROFILE_HEADER = "Personal Profile"
    OUR_CLIENTS_TRUST_US_PERSONAL_PROFILE_DESCRIPTION = "Link up to 10 TikTok accounts and set their subscriptions, " \
                                                        "save orders and manage them"
    OUR_CLIENTS_TRUST_US_CANCEL_ANYTIME_HEADER = "Cancel at Anytime"
    OUR_CLIENTS_TRUST_US_CANCEL_ANYTIME_DESCRIPTION = "Disable and cancel the promotion at any time. It will " \
                                                      "stop instantly"

    ANY_QUESTIONS_CONTAINER_HEADER = "ANY QUESTIONS?"
    ANY_QUESTIONS_DESCRIPTION = "Our services offer high-end promotion packages whose destiny is to power-up your " \
                                "TikTok presence. Boost to the element of your choice immediately —be it likes, " \
                                "views, and whatnot."
    ANY_QUESTIONS_MORE_INFO_BUTTON = "More info"
    ANY_QUESTIONS_CONTACT_US_BUTTON = "Contact us"


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