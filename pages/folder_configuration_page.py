from locators.folder_configuration_locators import FolderConfigurationLocators
from pages.base_page import BasePage


class FolderConfigurationPage(BasePage):
    locators = FolderConfigurationLocators()

    def create_folder_item(self, f_name, s_name):
        self.create_project_item(
            create_btn=self.locators.CREATE_NEW_ITEM_BNT_LOC,
            name_project=self.locators.ITEM_NAME_FIELD_LOC,
            item_type=self.locators.ITEM_TYPE_FOLDER,
            ok_btn=self.locators.OK_BTN_LOC,
            project_name=f_name
        )
        self.fill_text(self.locators.DISPLAY_NAME_FIELD_LOC, s_name)
        self.click_on_elem(self.locators.SAVE_BTN_LOC)
        self.click_on_elem(self.locators.ICON_BTN_LOC)
        text = self.get_text(self.locators.CREATED_JOB_LOC(f_name))
        return text
