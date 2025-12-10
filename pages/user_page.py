from data.dataclasses.create_user_dataclass import CreateUserDataClass
from locators.user_page_locators import UserPageLocators
from pages.base_page import BasePage


class UserPage(BasePage):

    locators = UserPageLocators()


    def create_user_v1(self, locator, user_info:CreateUserDataClass):


        self.fill_text(locator.USERNAME_FIELD_LOC, user_info.username)
        self.fill_text(locator.PASSWORD_FIELD_LOC, user_info.password)
        self.fill_text(locator.CONFIRM_PASSWORD_FIELD_LOC, user_info.password)
        self.fill_text(locator.FULLNAME_FIELD_LOC, user_info.fullname)
        self.fill_text(locator.EMAIL_FIELD_LOC, user_info.email)

    def create_user_v2(self, locator, username, password, confirm_password, fullname, email):

        self.fill_text(locator.USERNAME_FIELD_LOC, username)
        self.fill_text(locator.PASSWORD_FIELD_LOC, password)
        self.fill_text(locator.CONFIRM_PASSWORD_FIELD_LOC, confirm_password)
        self.fill_text(locator.FULLNAME_FIELD_LOC, fullname)
        self.fill_text(locator.EMAIL_FIELD_LOC, email)

    def create_user_v3(self, locator:UserPageLocators, username, password, confirm_password, fullname, email):

        self.fill_text(locator.USERNAME_FIELD_LOC, username)
        self.fill_text(locator.PASSWORD_FIELD_LOC, password)
        self.fill_text(locator.CONFIRM_PASSWORD_FIELD_LOC, confirm_password)
        self.fill_text(locator.FULLNAME_FIELD_LOC, fullname)
        self.fill_text(locator.EMAIL_FIELD_LOC, email)

    def create_user_v4(self, username, password, confirm_password, fullname, email):

        self.fill_text(self.locators.USERNAME_FIELD_LOC, username)
        self.fill_text(self.locators.PASSWORD_FIELD_LOC, password)
        self.fill_text(self.locators.CONFIRM_PASSWORD_FIELD_LOC, confirm_password)
        self.fill_text(self.locators.FULLNAME_FIELD_LOC, fullname)
        self.fill_text(self.locators.EMAIL_FIELD_LOC, email)