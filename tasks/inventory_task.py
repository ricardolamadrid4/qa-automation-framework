from pages.inventory_page_ui import InventoryPageUI
from interactions.interactions import PageInteractions

class InventoryTask:
    def __init__(self, driver):
        self.driver = driver
        self.interactions = PageInteractions(self.driver)
        
    def add_product_to_cart(self):
        self.interactions.click(InventoryPageUI.ADD_BACKPACK_BUTTON, 3)
        
    def get_cart_badge_value(self):
        return self.interactions.get_text(InventoryPageUI.CART_BADGE, 3)