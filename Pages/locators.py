from selenium.webdriver.common.by import By


class BasePageLocators:
    SIGNUP_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s"
                               " CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")
    HEADER_LOGO = (By.XPATH, "//a[@class='HeaderLogo_link__w6i5r']")
    HEADER = (By.XPATH, "//div[@class='HeaderTopWrapper_topWrapper__wcGqJ']")
    FOOTER = (By.XPATH, "//nav[@class='FooterNav_container__TNimz']")
    GET_FREE_VIEWS_PANEL = (By.XPATH, "//div[@class='HeaderBottomWrapper_bottomWrapper__w2dKr']")
    HOME_LINK_HEADER = (By.XPATH, "//div//header//ul//li[1]")
    PRICING_LINK_HEADER = (By.XPATH, "//div//header//ul//li[2]")
    FAQ_LINK_HEADER = (By.XPATH, "//div//header//ul//li[3]")
    CONTACT_US_LINK_HEADER = (By.XPATH, "//div//header//ul//li[4]")
    LEARN_LINK_HEADER = (By.XPATH, "//div//header//ul//li[5]")
    HOME_LINK_FOOTER = (By.XPATH, "//div//footer//ul//li[1]")
    PRICING_LINK_FOOTER = (By.XPATH, "//div//footer//ul//li[2]")
    FAQ_LINK_FOOTER = (By.XPATH, "//div//footer//ul//li[3]")
    CONTACT_US_LINK_FOOTER = (By.XPATH, "//div//footer//ul//li[4]")
    LEARN_LINK_FOOTER = (By.XPATH, "//div//footer//ul//li[5]")
    PRIVACY_POLICY_LINK = (By.XPATH, "//button[@class='ButtonTermsPrivacy_btn__12u2U"
                                     " ButtonTermsPrivacy_linkFooter__BtSNv'][1]")
    TERMS_CONDITIONS_LINK = (By.XPATH, "//button[@class='ButtonTermsPrivacy_btn__12u2U"
                                       " ButtonTermsPrivacy_linkFooter__BtSNv'][2]")
    EMAIL_ADDRESS_LINK = (By.XPATH, "//a[@class='ButtonTermsPrivacy_linkFooter__BtSNv'][1]")
    TELEGRAM_LINK = (By.XPATH, "//a[@class='ButtonTermsPrivacy_linkFooter__BtSNv'][2]")
    PRIVACY_POLICY_CONTAINER = (By.XPATH, "//div[@class='ModalBase_container__aKAn0 "
                                          "ModalBase_secondTerms_Policy__bi4Ks']")
    PRIVACY_POLICY_HEADER = (By.XPATH, "//article[@class='LayoutTermPrivacy_containerText__g__ZW']//h4")
    LEARN_CONTAINER = (By.XPATH, "//div[@class='ModalBase_container__aKAn0 "
                                 "ModalBase_colorBlack__FDws8 ModalBase_secondLearn__F77CZ']")


class HomePageLocators:
    BOOST_YOUR_TIKTOK_PROFILE_CONTAINER = (By.XPATH, "//section[@class='container HeaderOffer_headerOffer__0Nk4c']")
    BOOST_YOUR_TIKTOK_PROFILE_HEADER = (By.XPATH, "//h1[@class='HeaderOffer_title__XSSqh']")
    BOOST_YOUR_TIKTOK_PROFILE_DESCRIPTION = (By.XPATH, "//p[@class='HeaderOffer_description__0i_t7']")
    MAKE_AN_ORDER_BUTTON = (By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorRed2__33NJf']")
    HOW_IT_WORKS_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorRed__g7yY3 HeaderOffer"
                                     "_howItWorkButton__ajwBM']")
    WHAT_DO_WE_OFFER_CONTAINER = (By.XPATH, "//section[@class='container'][1]")
    WHAT_DO_WE_OFFER_HEADER = (By.XPATH, "//h2[@class='OurOffer_title__dM8j1']")
    WHAT_DO_WE_OFFER_GET_MORE_INFO_BUTTON = (By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorRed__y2rlJ"
                                                       " LinkButton_sizeBig__7aVP_']")
    WHAT_WE_HAVE_ALREADY_DONE_CONTAINER = (By.XPATH, "//section[@class='container DoneOrders_container__aI7tA']")
    WHAT_WE_HAVE_ALREADY_DONE_HEADER = (By.XPATH, "//h2[@class='DoneOrders_title__StHjc']")
    PROMOTION_FORMATS_CONTAINER = (By.XPATH, "//section[@class='container'][2]")
    PROMOTION_FORMATS_HEADER = (By.XPATH, "//h2[@class='PromotionFormats_title__fcjYc']")
    PROMOTION_FORMATS_GET_MORE_INFO_BUTTON = (By.XPATH, "//div[@class='PromotionFormatItem_container__f_OBE"
                                                        " PromotionFormatItem_containerGetMore__HuFNd']//a[@class="
                                                        "'LinkButton_link___jzSK LinkButton_colorWhite__A_Qx3']")
    OUR_CLIENTS_TRUST_US_CONTAINER = (By.XPATH, "//section[@class='container OurClients_container__rlkMW']")
    OUR_CLIENTS_TRUST_US_HEADER = (By.XPATH, "//h2[@class='OurClients_title__r45Yp']")
    ANY_QUESTIONS_CONTAINER = (By.XPATH, "//section[@class='container AnyQuestions_container__7229q']")
    ANY_QUESTIONS_HEADER = (By.XPATH, "//h2[@class='AnyQuestions_title__7gIg6']")
    ANY_QUESTIONS_DESCRIPTION = (By.XPATH, "//p[@class='AnyQuestions_description__x12kT']")
    ANY_QUESTIONS_MORE_INFO_BUTTON = (By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorBlack__WwvPN']")
    ANY_QUESTIONS_CONTACT_US_BUTTON = (By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorWhiteWithBorder_"
                                                 "_zLVqH']")


class PricingPageLocators:
    pass


class FaqPageLocators:
    POPULAR_QUESTIONS_CONTAINER = (By.XPATH, "//div[@class='FaqInfo_questionsContainer__20GJ_']")
    POPULAR_QUESTIONS_HEADER = (By.XPATH, "//h1[@class='FaqInfo_title__qU5w9']")
    FIRST_QUESTION_HEADER = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][1]//details//summary")
    FIRST_QUESTION_DESCRIPTION = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][1]//details/p")
    SECOND_QUESTION_HEADER = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][2]//details//summary")
    SECOND_QUESTION_DESCRIPTION = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][2]//details/p")
    THIRD_QUESTION_HEADER = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][3]//details//summary")
    THIRD_QUESTION_DESCRIPTION = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][3]//details/p")
    FOURTH_QUESTION_HEADER = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][4]//details//summary")
    FOURTH_QUESTION_DESCRIPTION = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][4]//details/p")
    FIFTH_QUESTION_HEADER = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][5]//details//summary")
    FIFTH_QUESTION_DESCRIPTION = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][5]//details/p")
    SIXTH_QUESTION_HEADER = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][6]//details//summary")
    SIXTH_QUESTION_DESCRIPTION = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][6]//details/p")
    SEVENTH_QUESTION_HEADER = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][7]//details//summary")
    SEVENTH_QUESTION_DESCRIPTION = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][7]//details/p")
    EIGHTH_QUESTION_HEADER = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][8]//details//summary")
    EIGHTH_QUESTION_DESCRIPTION = (By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][8]//details/p")


class ContactUsPageLocators:
    CONTACT_US_BANNER = (By.XPATH, "//figure[@class='SecondOffer_secondOffer__QlB2k']")
    CONTACT_US_CONTAINER_FORM = (By.XPATH, "//div[@class='ContactUsForm_containerForm__otErn']")
    GET_IN_TOUCH_HEADER = (By.XPATH, "//h1[@class='ContactUsForm_title__F_181']")
    GET_IN_TOUCH_DESCRIPTION = (By.XPATH, "//p[@class='ContactUsForm_description__XvG4f']")
    FIRST_NAME_TEXT_FIELD_HEADER = (By.XPATH, "//div[@class='InputContact_container__czJ87'][1]"
                                              "//p[@class='InputContact_title__UKNrS']")
    EMAIL_ADDRESS_TEXT_FIELD_HEADER = (By.XPATH, "//div[@class='InputContact_container__czJ87'][2]"
                                                 "//p[@class='InputContact_title__UKNrS']")
    MESSAGE_TEXT_AREA_HEADER = (By.XPATH, "//div[@class='InputContact_container__czJ87'][3]"
                                          "//p[@class='InputContact_title__UKNrS']")
    FIRST_NAME_TEXT_FIELD = (By.XPATH, "//input[@id='name']")
    EMAIL_ADDRESS_TEXT_FIELD = (By.XPATH, "//input[@id='email']")
    MESSAGE_TEXT_AREA = (By.XPATH, "//textarea[@id='message']")
    SEND_MESSAGE_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorRed__g7yY3']")
    EMAIL_ADDRESS_FIELD_REQUIRED_WARNING = (By.XPATH, "//div[@class='InputContact_container__czJ87'][2]"
                                                      "//p[@class='ErrorMessage_error__oBSER']")
    MESSAGE_TEXT_AREA_REQUIRED_WARNING = (By.XPATH, "//div[@class='InputContact_container__czJ87'][3]"
                                                    "//p[@class='ErrorMessage_error__oBSER']")
    PRIVACY_POLICY_BUTTON = (By.XPATH, "//button[@class='ButtonTermsPrivacy_btn__12u2U']")
    SUCCESS_SEND_MESSAGE_POPUP = (By.XPATH, "//div [@class='ModalBase_container__aKAn0 ModalBase_colorWhite__LRBeE"
                                            " ModalBase_typeModalSuccess__xIWgx']")
    SUCCESS_SEND_MESSAGE_TEXT = (By.XPATH, "//h4 [@class='ModalSuccess_title__EMOMJ']")
    MAX_LENGTH_FIRST_NAME_FIELD_WARNING = (By.XPATH, "//div[@class='InputContact_container__czJ87'][1]"
                                                     "//p[@class='ErrorMessage_error__oBSER']")


class LoginPageLocators:
    SIGNUP_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s"
                               " CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")
    SIGNUP_TAB = (By.XPATH, "//label[@class='AuthorizationTypeItem_label__DBPDq']")
    LOGIN_TAB = (By.XPATH, "//div[@class='AuthorizationTypeItem_item__2IwVY'][2]")
    GOOGLE_AUTH_BUTTON = (By.XPATH, "//button[@class='AuthorizationServices_btnLogin__txbzD "
                                    "AuthorizationServices_iconGoogle__4dy0a']")
    FACEBOOK_AUTH_BUTTON = (By.XPATH, "//button[@class='AuthorizationServices_btnLogin__txbzD "
                                      "AuthorizationServices_iconFacebook__0Fg5_']")
    INPUT_EMAIL = (By.ID, "authorizationEmail")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//button[@class='InputRoot_btnForgot__1AugM']")
    INPUT_PASSWORD = (By.ID, "authorizationPassword")
    SHOW_PASSWORD_ICON = (By.XPATH, "//div[@class='InputRoot_imgPassword__8Xy0k']")
    HIDE_PASSWORD_ICON = (By.XPATH, "//div[@class='InputRoot_imgPassword__8Xy0k InputRoot_imgPasswordVisible__xlKE6']")
    CREATE_MY_ACCOUNT_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorRed__g7yY3 "
                                          "CustomButton_typeAuth__m__ns']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s"
                              " CustomButton_colorAqua__TKZR6 CustomButton_typeAuth__m__ns']")
    CLOSE_LOGIN_PAGE_BUTTON = (By.XPATH, "//button[@class='ButtonClose_btn__rSXPy ButtonClose_btnDefault__3PgA1']")


class ForgotPasswordPageLocators:
    FORGOT_PASSWORD_FORM_HEADER = (By.XPATH, "//h3[@class='ModalBase_title__AecGk']")
    FORGOT_PASSWORD_FORM_DESCRIPTION = (By.XPATH, "//p[@class='ModalBase_forgotDescription__k5jiI']")
    YOUR_EMAIL_FIELD = (By.XPATH, "//input[@class='InputRoot_input__kEGzu InputRoot_inputForgot__UUMj1']")
    INVALID_EMAIL_WARNING = (By.XPATH, "//span[@class='ModalBase_errors__rYDQx']")
    NOT_REGISTERED_EMAIL_WARNING = (By.XPATH, "//span[@class='ModalBase_errors__rYDQx']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorBlack__4euz_ "
                               "CustomButton_btnForgot__rBSRC']")
    CLOSE_FORGOT_PASSWORD_BUTTON = (By.XPATH, "//*[@id='__next']/div/header/div[3]/div/div[5]/div/button")
    SUCCESS_FORM_HEADER = (By.XPATH, "//h3[@class='ModalDescriptionMessage_title__6hSBQ']")
    SUCCESS_FORM_DESCRIPTION_1 = (By.XPATH, "//p[@class='ModalDescriptionMessage_discription__FcfFh']")
    SUCCESS_FORM_DESCRIPTION_2 = (By.XPATH, "//p[@class='ModalDescriptionMessage_spam__k8MM0']")


class ProfilePageLocators:
    PROFILE_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 "
                                "CustomButton_btnSignUp__1ijqK ButtonHeaderProfile_button__756EG']")
    YOUR_PROFILE_TITLE = "//h2[@class='AccountComponent_title__gZO_n']"
    GENERAL_INFO_HEADER = "//h3[@class='UserProfile_title__LHdX8']"
    PROFILE_EMAIL = "//p[@class='UserProfile_email__Cj0km']"
    CHANGE_PASSWORD_BUTTON = "//a[@class='LinkButton_link___jzSK LinkButton_colorWhiteWithBorderAqua__S7MfE " \
                             "LinkButton_sizeSmall__Leg3Q']"
    LOG_OUT_BUTTON = "//a[@class='LinkButton_link___jzSK LinkButton_colorWhiteWithBorderAqua__S7MfE " \
                     "LinkButton_sizeSmall__Leg3Q']"
    MAKE_NEW_ORDER_BUTTON = "//a[@class='ButtonAddOrLink_wrapper__3G1F7 ButtonAddOrLink_typeImgSmall__CRumQ']"

    SWIPE_NAVIGATION_BUTTON_RIGHT = "//button[@class='SwiperNavigation_btn__zZaKt SwiperNavigation_btnRight__yBkxG']"
    SWIPE_NAVIGATION_BUTTON_LEFT = "//button[@class='SwiperNavigation_btn__zZaKt']"
    SWIPE_NAVIGATION_BUTTON_RIGHT_DISABLED = "//button[@class='SwiperNavigation_btn__zZaKt " \
                                             "SwiperNavigation_btnRight__yBkxG swiper-button-disabled']"
    SWIPE_NAVIGATION_BUTTON_LEFT_DISABLED = "//button[@class='SwiperNavigation_btn__zZaKt swiper-button-disabled']"


class ChangePasswordLocators:
    CHANGE_PASSWORD_TITLE = "//h1[@class='ChangePassword_title__oV8hO']"
    OLD_PASSWORD_TEXT_FIELD_HEADER = "//label[contains(text(), 'Old password')]"
    NEW_PASSWORD_TEXT_FIELD_HEADER = "//label[contains(text(), 'New password')]"
    CONFIRM_PASSWORD_TEXT_FIELD_HEADER = "//label[contains(text(), 'Confirm password')]"
    OLD_PASSWORD_TEXT_FIELD = "//input[@id='changPasswordOld']"
    NEW_PASSWORD_TEXT_FIELD = "//input[@id='changPasswordNew']"
    CONFIRM_PASSWORD_TEXT_FIELD = "//input[@id='changPasswordConfirm']"
    OLD_PASSWORD_WARNING_MESSAGE = "//div[@class='InputRoot_wrapper__sJ04b InputRoot_changePasswordForm__mTC_q']" \
                                   "[1]//span[@class='ModalBase_errors__rYDQx']"
    NEW_PASSWORD_WARNING_MESSAGE = "//div[@class='InputRoot_wrapper__sJ04b InputRoot_changePasswordForm__mTC_q']" \
                                   "[2]//span[@class='ModalBase_errors__rYDQx']"
    CONFIRM_PASSWORD_WARNING_MESSAGE = "//div[@class='InputRoot_wrapper__sJ04b']" \
                                       "//span[@class='ModalBase_errors__rYDQx']"
    CHANGE_BUTTON = "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 " \
                    "CustomButton_btnWhiteChangePassword__LZikD']"
    GO_BACK_BUTTON = "//button[@class='CustomButton_btn__22u2s CustomButton_colorBlack__4euz_ " \
                     "CustomButton_btnBlackChangePassword__rVM_5']"
