# coding: utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC

print("hello world")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)



driver.get('https://www.naukri.com/')


driver.implicitly_wait(1)
p = driver.current_window_handle
##############close all popups
chwd = driver.window_handles
for w in chwd:
#switch focus to child window
    if(w!=p):
        driver.switch_to.window(w)
        driver.close()
driver.switch_to.window(p)
############################






login_submit1='//*[@id="login_Layer"]/div'
driver.maximize_window() # For maximizing window
driver.implicitly_wait(5) # gives an implicit wait for 20 seconds
driver.find_element_by_xpath(login_submit1).click()
driver.implicitly_wait(5) # gives an implicit wait for 20 seconds

username_input='//*[@id="root"]/div[2]/div[2]/div/form/div[2]/input'
#driver.implicitly_wait(1)
password_input='//*[@id="root"]/div[2]/div[2]/div/form/div[3]/input'

#driver.implicitly_wait(0.5)
login_submit2='//*[@id="root"]/div[2]/div[2]/div/form/div[6]/button'
driver.implicitly_wait(1)
driver.find_element_by_xpath(username_input).send_keys('aniketsambher@gmail.com')
driver.implicitly_wait(1)
driver.find_element_by_xpath(password_input).send_keys('aniket12345')
driver.find_element_by_xpath(login_submit2).click()


#logged in

driver.implicitly_wait(3)
job='//*[@id="qsb-keyskill-sugg"]'
driver.find_element_by_xpath(job).send_keys('mongodb')
search='//*[@id="search-jobs"]/button'
driver.find_element_by_xpath(search).click()
#now applying for job 1
driver.implicitly_wait(3)

######note-the xpath for first job can't be automated so we have to state explicitly
job1='//*[@id="root"]/div[3]/div[2]/section[2]/div[2]/article[1]/div[1]/div/a'
driver.find_element_by_xpath(job1).click()
p = driver.current_window_handle
driver.switch_to.window(driver.window_handles[1])
print("current window title: " + driver.title)
driver.implicitly_wait(1)
job1_apply='//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[3]/div/button[2]'
driver.find_element_by_xpath(job1_apply).click()
driver.implicitly_wait(5)
try:
    driver.find_element_by_xpath('//*[@id="applyRelevanceFormSubmit"]').click()
    print("applied to job")
except:
    print("exception occured")  
driver.implicitly_wait(10)
driver.close()
driver.switch_to.window(p)

p = driver.current_window_handle
#now we start automating
for i in range(2,10):
    try:
    #now we handle the case where previous apply opens a new link we remove the newly opened webpages
        chwd = driver.window_handles
        for w in chwd:
            if(w!=p):
                driver.switch_to.window(w)
                driver.close()
        driver.switch_to.window(p)
        #####################################
        job_apply='//*[@id="root"]/div[3]/div[2]/section[2]/div[2]/article['+str(i)+']/div[1]/div/a'
        driver.find_element_by_xpath(job_apply).click()
        driver.switch_to.window(driver.window_handles[1])
        print("current window title: " + driver.title)
        driver.implicitly_wait(1)
        ####apply button for job application
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[3]/div/button[2]'))
        WebDriverWait(driver, 5).until(element_present)
        driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[3]/div/button[2]').click()
        #driver.find_element(By.XPATH, '//button[text()="APPLY"]').click()
        #applying='//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[3]/div/button[2]'
        #driver.find_element_by_xpath(applying).click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="applyRelevanceFormSubmit"]').click()
        print("applied to job")
        driver.implicitly_wait(30)
        driver.close()
        driver.switch_to.window(p)
    except:
        print("exception occured")
        continue

