from selenium import webdriver
import time
from behave import *
#from selenium.webdriver.common.keys import keys
@given("I am on the webpage")
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:\Program Files\selenium driver\chromedriver.exe")
    context.driver.implicitly_wait(3)
    context.driver.maximize_window()
    context.driver.get("http://demo.borland.com/InsuranceWebExtJS/index.jsf")

@when("I would enter valid credentials")
def step_impl(context):
    driver = context.driver
    context.driver.find_element_by_xpath("//*[@id='login-form:email']").send_keys("john.smith@gmail.com")
    context.driver.find_element_by_xpath("//*[@id='login-form:password']").send_keys("john")
    time.sleep(3)

@then("I click on login Button")
def step_impl(context):
    driver = context.driver
    context.driver.find_element_by_id("login-form:login").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//*[@id='logout-form:logout']").click()

@when("I would enter invalid emil and invalid password")
def step_impl(context):
    driver=context.driver
    context.driver.find_element_by_xpath("//*[@id='login-form:email']").clear()
    context.driver.find_element_by_xpath("//*[@id='login-form:email']").send_keys("johnsmithgmail.com")
    context.driver.find_element_by_xpath("//*[@id='login-form:password']").clear()
    context.driver.find_element_by_xpath("//*[@id='login-form:password']").send_keys("joh")
    context.driver.find_element_by_id("login-form:login").click()

    time.sleep(3)

@then("i should get error message")
def step_impl(context):
    driver=context.driver
    context.driver.find_element_by_xpath("//td[contains(text(),'Non-existing email, please try again.')]")
    time.sleep(5)
@when("I would enter valid email and invalid password")
def step_impl(context):
    driver=context.driver
    context.driver.find_element_by_xpath("//*[@id='login-form:email']").clear()
    context.driver.find_element_by_xpath("//*[@id='login-form:email']").send_keys("john.smith@gmail.com")
    context.driver.find_element_by_xpath("//*[@id='login-form:password']").clear()
    context.driver.find_element_by_xpath("//*[@id='login-form:password']").send_keys("joknnjnnjkj")
    context.driver.find_element_by_id("login-form:login").click()
    time.sleep(3)


@then("I should get error message stating invalid password")
def step_impl(context):
    driver=context.driver
    context.driver.find_element_by_xpath("//td[contains(text(),'Could not log in user: Internal Error')]")
    time.sleep(3)

@when("I would enter invalid email and valid password")
def step_impl(context):
    driver=context.driver
    context.driver.find_element_by_xpath("//*[@id='login-form:email']").clear()
    context.driver.find_element_by_xpath("//*[@id='login-form:email']").send_keys("johnsmithgmail.com")
    context.driver.find_element_by_xpath("//*[@id='login-form:password']").clear()
    context.driver.find_element_by_xpath("//*[@id='login-form:password']").send_keys("john")
    context.driver.find_element_by_id("login-form:login").click()

@then("I should get error message stating invalid email")
def step_impl(context):
    driver=context.driver
    context.driver.find_element_by_xpath("//td[contains(text(),'Non-existing email, please try again.')]")
    time.sleep(3)

@when("I would keep email field empty and enter valid password")
def step_impl(context):
    driver=context.driver
    context.driver.find_element_by_xpath("//*[@id='login-form:password']").clear()
    context.driver.find_element_by_xpath("//*[@id='login-form:password']").send_keys("john")
    context.driver.find_element_by_id("login-form:login").click()

@then("I should get error message stating please enter your email")
def step_impl(context):
    driver=context.driver
    context.driver.find_element_by_xpath("//td[contains(text(),'Please enter your e-mail')]")
    time.sleep(3)

@when("I would enter valid email and keep password field empty")
def step_impl(context):
    driver=context.driver
    context.driver.find_element_by_xpath("//*[@id='login-form:email']").clear()
    context.driver.find_element_by_xpath("//*[@id='login-form:email']").send_keys("johnsmithgmail.com")
    context.driver.find_element_by_id("login-form:login").click()
    time.sleep(3)

@then("I should get an error message stating please enter password")
def step_impl(context):
    driver=context.driver
    context.driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[2]/form/div[1]/table/tbody/tr/td")
    time.sleep(3)

@when("I would not enter email id and password and hit on login button")
def step_impl(context):
    driver=context.driver
    context.driver.find_element_by_id("login-form:login").click()
    time.sleep(2)

@then("I should get an error stating please enter email id and password")
def step_impl(context):
    context.driver.find_element_by_xpath("//td[contains(text(),'Please enter your e-mail')]")
    context.driver.find_element_by_xpath("//td[contains(text(),'Please enter your password')]")
    time.sleep(2)
    

