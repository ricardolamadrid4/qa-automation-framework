from selenium import webdriver
from assertions.login_assertions import LoginAssertions
from assertions.inventory_assertions import InventoryAssertions
from tasks.inventory_task import InventoryTask
from constants.environment_constants import EnvironmentConstants
from tasks.login_task import LoginTask

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    context.driver = webdriver.Chrome(options=options)
    context.driver.get(EnvironmentConstants.BASE_URL)
    
    context.login_task = LoginTask(context)
    context.login_assertions = LoginAssertions()
    context.inventory_task = InventoryTask(context)
    context.inventory_assertions = InventoryAssertions()
    
def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()

