import pytest
import requests
from playwright.sync_api import Playwright, ViewportSize


api_token = "114029fe295ca6dcd3add230c814da4a63"
user_name = "denis"
url = "http://localhost:8080/"

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


@pytest.fixture
def page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport=ViewportSize(width=1440, height=980),
        base_url="http://localhost:8080"
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

@pytest.fixture(scope="session", autouse=True)
def delete_jobs_after_all_tests():
    yield
    delete_jobs()