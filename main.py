# coding: utf-8

from selenium import webdriver

print("helwlo world")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

#chromedriver_location = webdriver.Chrome()


#driver = webdriver.Chrome(chromedriver_location)

driver.get('https://www.instagram.com/')
driver.maximize_window() # For maximizing window
driver.implicitly_wait(5) # gives an implicit wait for 20 seconds
username_input='//*[@id="loginForm"]/div/div[1]/div/label/input'
password_input='//*[@id="loginForm"]/div/div[2]/div/label/input'
login_submit='//*[@id="loginForm"]/div/div[3]'
driver.find_element_by_xpath(username_input).send_keys('username')
driver.find_element_by_xpath(password_input).send_keys('password')
driver.find_element_by_xpath(login_submit).click()