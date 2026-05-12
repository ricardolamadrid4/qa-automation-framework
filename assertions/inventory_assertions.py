from constants.inventory_constants import InventoryConstants

class InventoryAssertions:

    def verify_cart_badge_value(self, actual_value):
        assert actual_value == InventoryConstants.EXPECTED_CART_COUNT, \
        f"Expected {InventoryConstants.EXPECTED_CART_COUNT} but got {actual_value}"
    
    def verify_cart_is_empty(self, is_visible):
        assert is_visible is False, "Expected cart badge to be empty, but it is still visible"
    
    def verify_products_sorted_descending(self, product_names):
        assert product_names == sorted(product_names, reverse=True), f'Products are not sorted descending: {product_names}'