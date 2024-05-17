import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am logged in and on the profile page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.guru99.com/insurance/v1/index.php")

    # Log in
    context.driver.find_element(By.NAME, "email").send_keys("axle@example.com")
    context.driver.find_element(By.NAME, "password").send_keys("password")
    context.driver.find_element(By.NAME, "submit").click()

    # Navigate to the Profile page
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Profile')]").click()


@then('I should see my profile details')
def step_impl(context):
    profile_name = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user_profile_name"))
    )
    profile_email = context.driver.find_element(By.ID, "user_profile_email")
    profile_phone = context.driver.find_element(By.ID, "user_profile_phone")

    assert profile_name.get_attribute("value") != ""
    assert profile_email.get_attribute("value") != ""
    assert profile_phone.get_attribute("value") != ""


@when('I update my profile details')
def step_impl(context):
    name_input = context.driver.find_element(By.ID, "user_profile_name")
    email_input = context.driver.find_element(By.ID, "user_profile_email")
    phone_input = context.driver.find_element(By.ID, "user_profile_phone")

    name_input.clear()
    name_input.send_keys("New Name")

    email_input.clear()
    email_input.send_keys("new-email@example.com")

    phone_input.clear()
    phone_input.send_keys("1234567890")


@when('I save the changes')
def step_impl(context):
    save_button = context.driver.find_element(By.NAME, "commit")
    save_button.click()


@then('I should see the updated profile details')
def step_impl(context):
    updated_name = WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element_value((By.ID, "user_profile_name"), "New Name")
    )
    updated_email = WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element_value((By.ID, "user_profile_email"), "new-email@example.com")
    )
    updated_phone = WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element_value((By.ID, "user_profile_phone"), "1234567890")
    )

    assert context.driver.find_element(By.ID, "user_profile_name").get_attribute("value") == "New Name"
    assert context.driver.find_element(By.ID, "user_profile_email").get_attribute("value") == "new-email@example.com"
    assert context.driver.find_element(By.ID, "user_profile_phone").get_attribute("value") == "1234567890"


@then('I shut down the browser')
def close_browser(context):
    context.driver.quit()