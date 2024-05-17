import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the insurance website')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.guru99.com/insurance/v1/header.php")

@when('I click on the "Request Quotation" button')
def step_impl(context):
    request_quotation_button = context.driver.find_element(*(By.XPATH,"//a[@id='ui-id-2']"))
    request_quotation_button.click()

@when('I fill out the quotation form')
def step_impl(context):
    Breakdowncover = context.driver.find_element(By.ID, "quotation_breakdowncover")
    Breakdowncover.send_keys("At Home")
    Windscreenrepair = context.driver.find_element(By.ID, "quotation_windscreenrepair_t")
    Windscreenrepair.click()
    incidents = context.driver.find_element(By.ID, "quotation_incidents")
    incidents.send_keys("over speed in slow lane road")
    Registration = context.driver.find_element(By.NAME, "registration")
    Registration.send_keys("1state03 2554")
    Annual_mileage = context.driver.find_element(By.NAME, "mileage")
    Annual_mileage.send_keys("25 per mile")
    Estimated_value = context.driver.find_element(By.NAME, "value")
    Estimated_value.send_keys("2.5 million")
    Parking_Location = context.driver.find_element(By.NAME, "parkinglocation")
    Parking_Location.send_keys("Public Place")
    Star_of_policy_year = context.driver.find_element(By.NAME, "year")
    Star_of_policy_year.send_keys("1997")
    Star_of_policy_month = context.driver.find_element(By.NAME, "month")
    Star_of_policy_month.send_keys("07")
    Star_of_policy_day = context.driver.find_element(By.NAME, "date")
    Star_of_policy_day.send_keys("07")
    time.sleep(10)
    # Add other form fields as needed

@when('I click the submit')
def step_impl(context):
    submit_button = context.driver.find_element(By.NAME, "submit")
    submit_button.click()

@then('I should see a confirmation message')
def step_impl(context):
    confirmation_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "You have saved this quotation!"))
    )
    assert "Your quotation request has been submitted successfully" in confirmation_message.text
# You have saved this quotation!
# Your identification number is : 36017
@then('I remove the browser')
def step_impl(context):
    context.driver.quit()
