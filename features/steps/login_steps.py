from behave import then, when
from constants.environment_constants import EnvironmentConstants


@when('the user opens the login page')
def step_open_login_page(context):
    context.driver.get(EnvironmentConstants.BASE_URL)


@when('the user enters valid credentials')
def step_enter_valid_credentials(context):
    context.login_task.login_with_valid_credentials()
    
@then('the user should see the inventory page')
def step_verify_inventory_page(context):
    actual_title = context.login_task.get_inventory_page_title()
    context.login_assertions.verify_inventory_page_title(actual_title)