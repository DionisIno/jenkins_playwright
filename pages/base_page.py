from playwright.sync_api import Playwright, Page


class BasePage:

    def __init__(self, page: Page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url)

    def fill_text(self, loc, text_data):
        self.page.locator(loc).fill(text_data)

    def click_on_elem(self, loc):
        self.page.click(loc)

    def get_text(self, loc):
        text = self.page.locator(loc).text_content()
        return text

    def get_all_text(self, loc):
        text = self.page.locator(loc).all_text_contents()
        return text

    def create_project_item(self, name_project, create_btn, item_type, ok_btn, project_name):
        self.page.locator(create_btn).click()
        self.page.locator(name_project).fill(project_name)
        self.page.get_by_text(item_type, exact=True).click()
        self.page.click(ok_btn)
