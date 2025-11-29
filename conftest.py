import pytest
from playwright.sync_api import Playwright, ViewportSize


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