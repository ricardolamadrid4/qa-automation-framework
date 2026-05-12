from constants.inventory_constants import InventoryConstants

class LoginAssertions:
    
    def verify_inventory_page_title(self, actual_title):
        
        assert actual_title == InventoryConstants.INVENTORY_PAGE_TITLE, \
        f'Expected title: {InventoryConstants.INVENTORY_PAGE_TITLE}, but got: {actual_title}'