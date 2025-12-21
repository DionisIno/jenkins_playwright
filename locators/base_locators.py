

class BaseLocators:

    CREATE_NEW_ITEM_BNT_LOC = "a[href='/view/all/newJob']"
    ITEM_NAME_FIELD_LOC = "input[class='jenkins-input']"
    OK_BTN_LOC = "button[id='ok-button']"
    ICON_BTN_LOC = "img[id='jenkins-head-icon']"
    CREATED_JOB_LOC = lambda self, name: f"td > a[href='job/{name}/']"

    ITEM_TYPE_FOLDER = "Folder"