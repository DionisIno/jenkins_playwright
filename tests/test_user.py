import random
from data.generator.generator import CreateUserGenerator

generator = CreateUserGenerator()

def test_tc_15_001_01(page):
    user_info = next(generator.create_user_generator())

    page.goto("/manage/securityRealm/")

    create_user_btn = "a[href='addUser']"
    username_field_loc = "input[id='username']"
    password_field_loc = "input[name='password1']"
    confirm_password_field_loc = "input[name='password2']"
    fullname_field_loc = "input[name='fullname']"
    email_field_loc = "input[name='email']"
    save_user_btn_loc = "button[formnovalidate='formNoValidate']"
    created_user_loc = lambda name: f"td > a[href='user/{name.lower()}/']"

    page.click(create_user_btn)

    page.locator(username_field_loc).fill(user_info.username)
    page.locator(password_field_loc).fill(user_info.password)
    page.locator(confirm_password_field_loc).fill(user_info.password)
    page.locator(fullname_field_loc).fill(user_info.fullname)
    page.locator(email_field_loc).fill(user_info.email)

    page.click(save_user_btn_loc)

    text = page.locator(created_user_loc(user_info.username)).text_content()

    assert text == user_info.username