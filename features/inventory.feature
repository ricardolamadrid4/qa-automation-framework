Feature: Inventory

Scenario: Add product to cart
    When the user navigates to the inventory page
    And the user adds a product to the cart
    Then the user should see the cart badge updated to 1

Scenario: Remove product from cart
    When the user navigates to the inventory page
    And the user adds a product to the cart
    And the user removes the product from the cart
    Then the user should see the cart badge empty