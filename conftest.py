import pytest
import requests
from playwright.sync_api import Playwright, ViewportSize


api_token = "114029fe295ca6dcd3add230c814da4a63"
user_name = "denis"
url = "http://localhost:8080/"

@pytest.fixture(scope="session")
def get_cookies(playwright: Playwright):

    """Локаторы страницы логинки"""
    username_field_loc = "input[id='j_username']"
    password_field_loc = "input[id='j_password']"
    submit_btn_loc = "button[name='Submit']"
    """Сохраненные переменные"""
    username = "denis"
    password = "denis"

    browser = playwright.chromium.launch()
    context = browser.new_context(
        base_url="http://localhost:8080/login?from=%2F"
    )
    page = context.new_page()

    page.goto("/")
    """Страница логинки"""
    page.locator(username_field_loc).fill(username)
    page.locator(password_field_loc).fill(password)
    page.locator(submit_btn_loc).click()
    cookies = context.cookies()
    page.close()
    context.close()
    browser.close()
    return cookies



@pytest.fixture
def page(playwright: Playwright, get_cookies):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport=ViewportSize(width=1440, height=980),
        base_url="http://localhost:8080"
    )
    context.add_cookies(get_cookies)
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

def get_all_jobs():
    response = requests.get(
        url=f"{url}api/json",
        auth=(user_name, api_token)
    )
    return response.json()['jobs']

def delete_jobs():
    jobs_list = get_all_jobs()

    for job in jobs_list:
        name = job["name"]
        requests.post(
            url=f"{url}/job/{name}/doDelete",
            auth=(user_name, api_token)
        )

@pytest.fixture(scope="session", autouse=True)
def delete_jobs_after_all_tests():
    yield
    delete_jobs()