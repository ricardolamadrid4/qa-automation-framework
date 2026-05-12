from selenium.webdriver.common.by import By 

class InventoryPageUI:
    
    PRODUCTS_TITLE = (By.CLASS_NAME, 'title')
    ADD_BACKPACK_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    REMOVE_BACKPACK_BUTTON = (By.ID, 'remove-sauce-labs-backpack')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    SORT_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')
    PRODUCT_NAMES = (By.CLASS_NAME, 'inventory_item_name')