import random


def test_tc_21_010_002(page):

    page.goto("/")

    random_text = f"Denis-{random.randint(0, 99999999)}-Denis"

    add_description_btn_loc = "a[id='description-link']"
    description_field_loc = "textarea[name='description']"
    save_btn_loc = "button[formnovalidate='formNoValidate']"

    description_text_loc = "div[id='description-content']"

    page.click(add_description_btn_loc)
    page.locator(description_field_loc).fill(random_text)
    page.locator(save_btn_loc).click()

    text = page.locator(description_text_loc).inner_text()

    assert text == random_text