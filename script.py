from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from time import sleep
driver = webdriver.Chrome()
driver.get("https://kurs.kz")

driver.find_element_by_css_selector("input[type='text'][name='login']").send_keys(sys.argv[0])

driver.find_element_by_css_selector("input[type='password'][name='pwd']").send_keys(sys.argv[1])
driver.find_element_by_css_selector("input[type='submit'][value='enter']").send_keys(Keys.RETURN)

sleep(1)

driver.find_element_by_css_selector("input[type='submit'][class='submit-button']").send_keys(Keys.RETURN)