from selenium import webdriver
import time


driver = webdriver.Chrome("C:\\chromedriver")

driver.get("https://www.instagram.com/")
time.sleep(3)
driver.find_element_by_name("username").send_keys("error_terminator")
time.sleep(2)
driver.find_element_by_name("password").send_keys("error_terminator")
time.sleep(1)
driver.find_element_by_xpath("//div[text()='Log In']").click()

