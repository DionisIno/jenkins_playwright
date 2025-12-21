import time

from data.endpoints import Endpoints
from pages.folder_configuration_page import FolderConfigurationPage


class TestDisplayNameAndDDescription:
    endpoint = Endpoints()

    def test_set_display_name_for_folder(self, page):
        f_name = "Denis1223"
        s_name = "Luma1234"

        folder_page = FolderConfigurationPage(page, self.endpoint.MAIN_PAGE_ENDPOINT)
        folder_page.open()
        text = folder_page.create_folder_item(f_name, s_name)
        assert text == s_name