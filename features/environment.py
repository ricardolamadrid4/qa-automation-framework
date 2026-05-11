from selenium import webdriver
from constants.environment_constants import EnvironmentConstants
from tasks.login_task import LoginTask
from tasks.inventory_task import InventoryTask
from assertions.login_assertions import LoginAssertions
from assertions.inventory_assertions import InventoryAssertions


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--incognito')

    context.driver = webdriver.Chrome(options=options)
    context.driver.get(EnvironmentConstants.BASE_URL)

    # Tasks
    context.login_task = LoginTask(context)
    context.inventory_task = InventoryTask(context)

    # Assertions
    context.login_assertions = LoginAssertions()
    context.inventory_assertions = InventoryAssertions()


def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()

