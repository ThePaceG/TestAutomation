import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the retrieve quotation page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.guru99.com/insurance/v1/header.php")
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Retrieve Quotation')]").click()

@when('I fill out the quotation retrieval form')
def step_impl(context):
    policy_number_input = context.driver.find_element(By.NAME, "policyid")
    policy_number_input.send_keys("36017")
time.sleep(25)
@when('I click the Retrieve')
def step_impl(context):
    submit_button = context.driver.find_element(By.ID, "getquote")
    submit_button.click()

@then('I should see the retrieved quotation details')
def step_impl(context):
    # Assuming the quotation details are displayed on the page after form submission
    quotation_details = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "container-fluid"))
    )
    # Modify the assertion based on the actual text or structure of quotation details
    assert "Quotation Details" in quotation_details.text

@then('I shut down the browser')
def close_browser(context):
    context.driver.quit()
