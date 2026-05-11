from constants.main_section_constants import MainSectionConstants

class InventoryAssertions:

    def verify_cart_badge_value(self, actual_value):
        assert actual_value == MainSectionConstants.EXPECTED_CART_COUNT, \
        f"Expected {MainSectionConstants.EXPECTED_CART_COUNT} but got {actual_value}"
    
    def verify_cart_is_empty(self, is_visible):
        assert is_visible is False, "Expected cart badge to be empty, but it is still visible"