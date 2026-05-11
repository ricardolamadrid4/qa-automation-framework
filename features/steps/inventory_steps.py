from behave import when, then


@when('the user navigates to the inventory page')
def step_navigate_to_inventory_page(context):
    context.login_task.login_with_valid_credentials()
    
@when('the user adds a product to the cart')
def step_add_product_to_cart(context):
    context.inventory_task.add_product_to_cart()
    
@then('the user should see the cart badge updated to 1')
def step_verify_cart_badge(context):
    actual_cart_count = context.inventory_task.get_cart_badge_value()
    context.inventory_assertions.verify_cart_badge_value(actual_cart_count)
    
@when("the user removes the product from the cart")
def step_remove_product(context):
    context.inventory_task.remove_product_from_cart()


@then("the user should see the cart badge empty")
def step_verify_empty_cart(context):
    is_visible = context.inventory_task.is_cart_badge_displayed()
    context.inventory_assertions.verify_cart_is_empty(is_visible)