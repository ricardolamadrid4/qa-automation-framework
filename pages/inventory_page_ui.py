from selenium.webdriver.common.by import By 

class InventoryPageUI:
    
    PRODUCTS_TITLE = (By.CLASS_NAME, 'title')
    ADD_BACKPACK_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')