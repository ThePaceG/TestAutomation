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
    # context.driver.find_element(By.XPATH, "//a[@id='ui-id-4']").click()
    context.driver.find_element(By.XPATH, "//a[@id='ui-id-5']").click()
    time.sleep(10)

@then('I should see my profile details')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[@id='ui-id-5']").click()
@when('I update my profile details')
def step_impl(context):
    context.driver.find_element(By.ID, "user_title").send_keys("MR")
    context.driver.find_element(By.ID, "user_firstname").send_keys("Axle")
    context.driver.find_element(By.ID, "user_surname").send_keys("Dynamite")
    context.driver.find_element(By.ID, "user_phone").send_keys("981234567")
    context.driver.find_element(By.ID, "user_dateofbirth_2i").send_keys("07")
    context.driver.find_element(By.ID, "user_dateofbirth_3i").send_keys("12")
    context.driver.find_element(By.ID, "user_dateofbirth_1i").send_keys("1997")
    context.driver.find_element(By.ID, "user_licencetype_t").click()
    context.driver.find_element(By.ID, "user_licenceperiod").send_keys("10")
    context.driver.find_element(By.ID, "user_occupation_id").send_keys("Engineer")
    context.driver.find_element(By.ID, "user_address_attributes_street").send_keys("swoyambhu")
    context.driver.find_element(By.ID, "user_address_attributes_city").send_keys("Kathmandu")
    context.driver.find_element(By.ID, "user_address_attributes_county").send_keys("Nepal")
    context.driver.find_element(By.ID, "user_address_attributes_postcode").send_keys("12345")
    # context.driver.find_element(By.ID, "user_user_detail_attributes_email").send_keys("axle@example.com")
    # context.driver.find_element(By.ID, "user_user_detail_attributes_password").send_keys("password")
    # context.driver.find_element(By.ID, "user_user_detail_attributes_password_confirmation").send_keys("password")
    # Submit the form
    context.driver.find_element(By.NAME, "commit").click()
    time.sleep(20)
@when('I save the changes')
def step_impl(context):
    save_button = context.driver.find_element(By.NAME, "commit")
    save_button.click()


@then('I should see the updated profile details')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@id='ui-id-4']").click()
time.sleep(20)
@then('I shut down the browser')
def close_browser(context):
    context.driver.quit()