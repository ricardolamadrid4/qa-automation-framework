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

Scenario: Sort products by name Z to A
    When the user navigates to the inventory page
    And the user sorts products by name Z to A
    Then the products should be displayed in descending alphabetical order

Scenario: Complete checkout process
    When the user navigates to the inventory page
    And the user adds a product to the cart
    And the user proceeds to checkout
    And the user enters checkout information
    And the user completes the purchase
    Then the user should see the checkout complete message