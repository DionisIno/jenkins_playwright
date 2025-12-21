from locators.base_locators import BaseLocators


class FolderConfigurationLocators(BaseLocators):

    DISPLAY_NAME_FIELD_LOC = "input[name='_.displayNameOrNull']"
    SAVE_BTN_LOC = "button[formnovalidate='formNoValidate']"