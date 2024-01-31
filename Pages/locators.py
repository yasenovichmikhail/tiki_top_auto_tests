from selenium.webdriver.common.by import By


class BasePageLocators:
    SIGNUP_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s"
                               " CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")
    HEADER_LOGO = (By.XPATH, "//a[@class='HeaderLogo_link__w6i5r']")
    HEADER = (By.XPATH, "//div[@class='HeaderTopWrapper_topWrapper__wcGqJ']")
    FOOTER = (By.XPATH, "//nav[@class='FooterNav_container__TNimz']")
    GET_FREE_VIEWS = (By.XPATH, "//div[@class='HeaderBottomWrapper_bottomWrapper__w2dKr']")
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
    MAKE_AN_ORDER_BUTTON = (By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorRed2__33NJf']")
    HOW_IT_WORKS_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorRed__g7yY3 HeaderOffer"
                                     "_howItWorkButton__ajwBM']")
    BOOST_YOUR_TIKTOK_PROFILE_CONTAINER = (By.XPATH, "//section[@class='container HeaderOffer_headerOffer__0Nk4c']")
    BOOST_YOUR_TIKTOK_PROFILE_HEADER = (By.XPATH, "//h1[@class='HeaderOffer_title__XSSqh']")
    BOOST_YOUR_TIKTOK_PROFILE_DESCRIPTION = (By.XPATH, "//p[@class='HeaderOffer_description__0i_t7']")
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
    LOGIN_TAB = (By.XPATH, "//div[@class='AuthorizationTypeItem_item__2IwVY'][2]")
    INPUT_EMAIL = (By.ID, "authorizationEmail")
    INPUT_PASSWORD = (By.ID, "authorizationPassword")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s"
                              " CustomButton_colorAqua__TKZR6 CustomButton_typeAuth__m__ns']")
