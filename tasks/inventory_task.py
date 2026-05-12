from constants.inventory_constants import InventoryConstants
from pages.inventory_page_ui import InventoryPageUI
from interactions.interactions import PageInteractions
from selenium.webdriver.support.ui import Select


class InventoryTask:
    def __init__(self, driver):
        self.driver = driver
        self.interactions = PageInteractions(self.driver)
        
    def add_product_to_cart(self):
        self.interactions.click(InventoryPageUI.ADD_BACKPACK_BUTTON, 1)
        
    def get_cart_badge_value(self):
        return self.interactions.get_text(InventoryPageUI.CART_BADGE, 1)
    
    def remove_product_from_cart(self):
        self.interactions.click(InventoryPageUI.REMOVE_BACKPACK_BUTTON, 1)
        
    def is_cart_badge_displayed(self):
        return self.interactions.verify_element_is_visible(InventoryPageUI.CART_BADGE, 1)
    
    def sort_products_by_name_descending(self):
        sort_dropdown = Select(self.interactions.find_element(InventoryPageUI.SORT_DROPDOWN, 1))
        sort_dropdown.select_by_visible_text(InventoryConstants.PRODUCT_SORT_NAME_Z_TO_A)

        
    def get_product_names(self):
        product_elements = self.interactions.find_elements(InventoryPageUI.PRODUCT_NAMES)
        
        return [product.text for product in product_elements]
    
    def proceed_to_checkout(self):
        self.interactions.click(InventoryPageUI.CART_BUTTON, 1)
        self.interactions.click(InventoryPageUI.CHECKOUT_BUTTON, 1)
        
    def enter_checkout_information(self):
        self.interactions.enter_text(InventoryPageUI.CHECKOUT_INFORMATION['first_name'],
        InventoryConstants.TEST_FIRST_NAME, 1)

        self.interactions.enter_text(InventoryPageUI.CHECKOUT_INFORMATION['last_name'],
        InventoryConstants.TEST_LAST_NAME, 1)

        self.interactions.enter_text(InventoryPageUI.CHECKOUT_INFORMATION['postal_code'],
        InventoryConstants.TEST_POSTAL_CODE, 1)

        self.interactions.click(InventoryPageUI.CONTINUE_BUTTON, 1)
        
    def complete_purchase(self):
        self.interactions.click(InventoryPageUI.FINISH_BUTTON, 1)
        
    def get_checkout_complete_message(self):
        return self.interactions.get_text(InventoryPageUI.CHECKOUT_COMPLETE_MESSAGE, 1)