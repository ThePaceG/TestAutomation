from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I navigate to the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.guru99.com/insurance/v1/index.php")


@when('I enter correct username and password')
def step_impl(context):
    username_input = context.driver.find_element(By.NAME, "email")
    password_input = context.driver.find_element(By.NAME, "password")
    username_input.send_keys("axle@example.com")  # Replace with your correct username
    password_input.send_keys("password")  # Replace with your correct password


@when('I click on the submit button')
def step_impl(context):
    login_button = context.driver.find_element(By.NAME, "submit")
    login_button.click()


@then('I should see the dashboard page')
def step_impl(context):
    # Wait for an element on the dashboard page to ensure successful login
    dashboard_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "menu"))
    )
    # Assert that the dashboard element is visible
    assert dashboard_element.is_displayed(), "Dashboard page not displayed after successful login"


@then('I close the browser')
def close_browser(context):
    context.driver.quit()
