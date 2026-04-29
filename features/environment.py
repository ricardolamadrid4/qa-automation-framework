from selenium import webdriver
from assertions.login_assertions import LoginAssertions
from tasks.login_task import LoginTask

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    context.driver = webdriver.Chrome(options=options)
    
    context.login_task = LoginTask(context)
    context.login_assertions = LoginAssertions()
    
def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()

