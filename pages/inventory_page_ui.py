from selenium.webdriver.common.by import By 

class InventoryPageUI:
    
    PRODUCTS_TITLE = (By.CLASS_NAME, 'title')
    ADD_BACKPACK_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    REMOVE_BACKPACK_BUTTON = (By.ID, 'remove-sauce-labs-backpack')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    SORT_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')
    PRODUCT_NAMES = (By.CLASS_NAME, 'inventory_item_name')
    
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    CHECKOUT_INFORMATION = {
    'first_name': (By.ID, 'first-name'),
    'last_name': (By.ID, 'last-name'),
    'postal_code': (By.ID, 'postal-code')
}

    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')

    CHECKOUT_COMPLETE_MESSAGE = (By.CLASS_NAME, 'complete-header')