from constants.inventory_constants import InventoryConstants
from pages.inventory_page_ui import InventoryPageUI
from interactions.interactions import PageInteractions
from selenium.webdriver.support.ui import Select


class InventoryTask:
    def __init__(self, driver):
        self.driver = driver
        self.interactions = PageInteractions(self.driver)
        
    def add_product_to_cart(self):
        self.interactions.click(InventoryPageUI.ADD_BACKPACK_BUTTON, 3)
        
    def get_cart_badge_value(self):
        return self.interactions.get_text(InventoryPageUI.CART_BADGE, 3)
    
    def remove_product_from_cart(self):
        self.interactions.click(InventoryPageUI.REMOVE_BACKPACK_BUTTON, 3)
        
    def is_cart_badge_displayed(self):
        return self.interactions.verify_element_is_visible(InventoryPageUI.CART_BADGE, 3)
    
    def sort_products_by_name_descending(self):
        sort_dropdown = Select(self.interactions.find_element(InventoryPageUI.SORT_DROPDOWN, 3))
        sort_dropdown.select_by_visible_text(InventoryConstants.PRODUCT_SORT_NAME_Z_TO_A)

        
    def get_product_names(self):
        product_elements = self.interactions.find_elements(InventoryPageUI.PRODUCT_NAMES)
        
        return [product.text for product in product_elements]