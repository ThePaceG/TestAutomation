from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the login page')
def step_impl(context):
        context.driver = webdriver.Chrome()
        context.driver.get("https://demo.guru99.com/insurance/v1/index.php")

@when('I enter incorrect username and password')
def step_impl(context):
        username_input = context.driver.find_element(By.NAME, "email")
        password_input = context.driver.find_element(By.NAME, "password")
        username_input.send_keys("incorrect-user")
        password_input.send_keys("incorrect-password")

@when('I click on the login button')
def step_impl(context):
        login_button = context.driver.find_element(By.NAME, "submit")
        login_button.click()

@then('I should see an error message')
def step_impl(context):
        error_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-form"))
     )
        assert "Enter your Email address and password correct" in error_message.text

@then('I quit the browser')
def close_browser(context):
        context.driver.quit()

