

class UserPageLocators:

    CREATE_USER_BTN = "a[href='addUser']"
    USERNAME_FIELD_LOC = "input[id='username']"
    PASSWORD_FIELD_LOC = "input[name='password1']"
    CONFIRM_PASSWORD_FIELD_LOC = "input[name='password2']"
    FULLNAME_FIELD_LOC = "input[name='fullname']"
    EMAIL_FIELD_LOC = "input[name='email']"
    SAVE_USER_BTN_LOC = "button[formnovalidate='formNoValidate']"
    CREATED_USER_LOC = lambda self, name: f"td > a[href='user/{name.lower()}/']"
    ERROR_TEXT_LOC = "div.error"
