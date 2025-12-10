import random
import time


def get_name_loc(name):
    return f"td > a[href='job/{name}/']"


def test_tc_01_001_01(page):
    """Переходим по ссылке"""
    page.goto("/")

    """Сохраненные переменные"""
    new_item_name = f"denis-{random.randint(0, 9999999)}"

    """Локатор для кнопки + new item"""
    new_item_btn_loc = "a[href='/view/all/newJob']"

    """Локаторы страницы создания new item"""
    item_name_field_loc = "input[class='jenkins-input']"
    item_type_text = "Pipeline"
    ok_btn_loc = "button[id='ok-button']"

    """Локатор для лого"""
    logo_loc = "a[class='app-jenkins-logo']"

    """Локатор для созданного item"""
    created_item_loc = lambda name: f"td > a[href='job/{name}/']"

    """Клик по кнопке + new item"""
    page.locator(new_item_btn_loc).click()

    """Страница создания нового item"""
    page.locator(item_name_field_loc).fill(new_item_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_btn_loc).click()

    """Клик по лого"""
    page.locator(logo_loc).click()

    """Получение текста созданного item"""
    text = page.locator(created_item_loc(new_item_name)).text_content()
    # text = page.locator(get_name_loc(new_item_name)).text_content()

    assert text == new_item_name


