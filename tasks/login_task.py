from interactions.interactions import PageInteractions
from pages.login_page_ui import LoginPageUI
from pages.inventory_page_ui import InventoryPageUI
from constants.login_constants import LoginConstants


class LoginTask:

    def __init__(self, context):
        self.context = context
        self.interactions = PageInteractions(context)


    def login_with_valid_credentials(self):
        
        self.interactions.enter_text(LoginPageUI.LOGIN_FORM['username'], LoginConstants.USERNAME, 3)
        self.interactions.enter_text(LoginPageUI.LOGIN_FORM['password'], LoginConstants.PASSWORD, 3)
        self.interactions.click(LoginPageUI.LOGIN_FORM['login_button'], 3)
    
    def get_inventory_page_title(self):
        return self.interactions.get_text(InventoryPageUI.PRODUCTS_TITLE)