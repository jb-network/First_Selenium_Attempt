from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')

input1Path = "input[id='ipt1']"
input1Element = browser.find_element(By.CSS_SELECTOR, input1Path)
input1Element.send_keys("This is an automation test.")
