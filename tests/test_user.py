from data.endpoints import Endpoints
from data.error_message import ErrorMessage
from data.generator.user_generator import CreateUserGenerator
from locators.user_page_locators import UserPageLocators
from pages.user_page import UserPage
from src.assertions import Assertions


class TestCreateUser:

    generator = CreateUserGenerator()
    locator = UserPageLocators()
    endpoint = Endpoints()
    assertions = Assertions()
    error_message = ErrorMessage()

    def test_tc_15_001_01_v1(self, page):
        user_info = next(self.generator.create_user_generator())
        user_page = UserPage(page, self.endpoint.CREATE_USER_ENDPOINT)

        user_page.open()

        user_page.click_on_elem(self.locator.CREATE_USER_BTN)

        user_page.fill_text(self.locator.USERNAME_FIELD_LOC, user_info.username)
        user_page.fill_text(self.locator.PASSWORD_FIELD_LOC, user_info.password)
        user_page.fill_text(self.locator.CONFIRM_PASSWORD_FIELD_LOC, user_info.password)
        user_page.fill_text(self.locator.FULLNAME_FIELD_LOC, user_info.fullname)
        user_page.fill_text(self.locator.EMAIL_FIELD_LOC, user_info.email)

        user_page.click_on_elem(self.locator.SAVE_USER_BTN_LOC)

        text = user_page.get_text(self.locator.CREATED_USER_LOC(user_info.username))

        self.assertions.assert_text(text, user_info.username)

    def test_tc_15_001_01_v2(self, page):
        user_info = next(self.generator.create_user_generator())

        user_page = UserPage(page, self.endpoint.CREATE_USER_ENDPOINT)
        user_page.open()

        user_page.click_on_elem(self.locator.CREATE_USER_BTN)

        user_page.create_user_v1(self.locator, user_info)
        user_page.click_on_elem(self.locator.SAVE_USER_BTN_LOC)

        text = user_page.get_text(self.locator.CREATED_USER_LOC(user_info.username))

        self.assertions.assert_text(text, user_info.username)

    def test_tc_15_001_01_v3(self, page):
        user_info = next(self.generator.create_user_generator())

        user_page = UserPage(page, self.endpoint.CREATE_USER_ENDPOINT)
        user_page.open()

        user_page.click_on_elem(self.locator.CREATE_USER_BTN)

        user_page.create_user_v2(
            locator=self.locator,
            username=user_info.username,
            password=user_info.password,
            confirm_password=user_info.password,
            fullname=user_info.fullname,
            email=user_info.email
        )
        user_page.click_on_elem(self.locator.SAVE_USER_BTN_LOC)

        text = user_page.get_text(self.locator.CREATED_USER_LOC(user_info.username))

        self.assertions.assert_text(text, user_info.username)

    def test_tc_15_001_01_v4(self, page):
        user_info = next(self.generator.create_user_generator())

        user_page = UserPage(page, self.endpoint.CREATE_USER_ENDPOINT)
        user_page.open()

        user_page.click_on_elem(self.locator.CREATE_USER_BTN)

        user_page.create_user_v2(
            locator=self.locator,
            username=user_info.username,
            password=user_info.password,
            confirm_password=user_info.password,
            fullname=user_info.fullname,
            email=str(self.generator.random_int)
        )

        user_page.click_on_elem(self.locator.SAVE_USER_BTN_LOC)

        text = user_page.get_text(self.locator.ERROR_TEXT_LOC)

        self.assertions.assert_text(text, self.error_message.error_email_message)

    def test_tc_15_001_01_v5(self, page):
        user_info = next(self.generator.create_user_generator())

        user_page = UserPage(page, self.endpoint.CREATE_USER_ENDPOINT)
        user_page.open()

        user_page.click_on_elem(self.locator.CREATE_USER_BTN)

        user_page.create_user_v2(
            locator=self.locator,
            username=user_info.username,
            password=user_info.password,
            confirm_password=user_info.confirm_password,
            fullname=user_info.fullname,
            email=user_info.email
        )

        user_page.click_on_elem(self.locator.SAVE_USER_BTN_LOC)

        text = user_page.get_all_text(self.locator.ERROR_TEXT_LOC)

        assert len(text) == 2
        a = set(text)
        assert len(a) == 1

        self.assertions.assert_text(*a, self.error_message.error_password_message)


    def test_tc_15_001_01_v6(self, page):
        user_info = next(self.generator.create_user_generator())

        user_page = UserPage(page, self.endpoint.CREATE_USER_ENDPOINT)
        user_page.open()

        user_page.click_on_elem(self.locator.CREATE_USER_BTN)

        user_page.create_user_v4(
            username=user_info.username,
            password=user_info.password,
            confirm_password=user_info.password,
            fullname=user_info.fullname,
            email=user_info.email
        )
        user_page.click_on_elem(self.locator.SAVE_USER_BTN_LOC)

        text = user_page.get_text(self.locator.CREATED_USER_LOC(user_info.username))

        self.assertions.assert_text(text, user_info.username)