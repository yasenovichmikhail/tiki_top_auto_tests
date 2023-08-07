from selenium.webdriver.common.by import By

class BasePageLocators:
    SIGNUP_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")
    HEADER_LOGO = (By.XPATH, "//a[@class='HeaderLogo_link__w6i5r']")


class HomePage:
    MAKE_AN_ORDER_BUTTON = (By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorRed2__33NJf']")
    HOW_IT_WORKS_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorRed__g7yY3 HeaderOffer_howItWorkButton__ajwBM']")
    GET_MORE_INFO_BUTTON1 = (By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorRed__y2rlJ LinkButton_sizeBig__7aVP_']")
    GET_MORE_INFO_BUTTON2 = (By.XPATH, "//div[@class='PromotionFormatItem_container__f_OBE PromotionFormatItem_containerGetMore__HuFNd']//a[@class='LinkButton_link___jzSK LinkButton_colorWhite__A_Qx3']")
    ANY_QUESTIONS_MORE_INFO_BUTTON = (By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorBlack__WwvPN']")
    ANY_QUESTIONS_CONTACT_US_BUTTON = (By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorWhiteWithBorder__zLVqH']")
    BOOST_YOUR_TIKTOK_PROFILE_CONTAINER = (By.XPATH, "//section[@class='container HeaderOffer_headerOffer__0Nk4c']")
    WHAT_DO_WE_OFFER_CONTAINER = (By.XPATH, "//section[@class='container'][1]")
    PROMOTION_FORMATS_CONTAINER = (By.XPATH, "//section[@class='container'][2]")
    OUR_CLIENTS_TRUST_US_CONTAINER = (By.XPATH, "//section[@class='container OurClients_container__rlkMW']")
    ANY_QUESTIONS_CONTAINER = (By.XPATH, "//section[@class='container AnyQuestions_container__7229q']")


class PricingPage:


class FaqPage:


class ContactUsPage:


class LoginPage:
    """Locators"""
    SIGNUP_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")

    LOGIN_TAB = (By.XPATH, "//div[@class='AuthorizationTypeItem_item__2IwVY'][2]")

    INPUT_EMAIL = (By.ID, "authorizationEmail")

    INPUT_PASSWORD = (By.ID, "authorizationPassword")

    LOGIN_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorAqua__TKZR6 CustomButton_typeAuth__m__ns']")
