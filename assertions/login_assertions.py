from constants.main_section_constants import MainSectionConstants

class LoginAssertions:
    
    def verify_inventory_page_title(self, actual_title):
        
        assert actual_title == MainSectionConstants.INVENTORY_PAGE_TITLE, \
        f'Expected title: {MainSectionConstants.INVENTORY_PAGE_TITLE}, but got: {actual_title}'