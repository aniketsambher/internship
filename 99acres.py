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
driver.get('https://www.99acres.com/')

driver.find_element_by_xpath('//*[@id="keyword"]').send_keys('delhi')
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="keyword"]').send_keys(Keys.ENTER)


#//*[@id="srp_tuple_price"]
driver.maximize_window()
#element = driver.find_element_by_xpath("class_name").text
driver.implicitly_wait(10)
list1=[]
j=2
while True:
    
    for i in range(1,30):
        a=[]
        try:
            element1 = driver.find_element_by_xpath('(//*[@id="srp_tuple_price"])'+'['+str(i)+']').text
            element1=element1.splitlines()[0]
            if element1.find('Cr') != -1:
                price=float(element1.split(' ')[1])*100
            else :
                price=float(element1.split(' ')[1])
        except:
            price=-1
        #print(price)
        try:
            element2 = driver.find_element_by_xpath('(//*[@id="srp_tuple_primary_area"])'+'['+str(i)+']').text
            area=float(element2.split(' ')[0].replace(',','').replace('-',''))
        except:
            area=-1
        try:
            element3 = driver.find_element_by_xpath('(//*[@id="srp_tuple_bedroom"])'+'['+str(i)+']').text
            bhk=float(element3.split(' ')[0])
        except:
            bhk=-1
        a.append([price,area,bhk])
        list1.append(a)
        #print(list1)
    j=j+1
    print(j)
    driver.implicitly_wait(5)
    if (j<=3):
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[4]/div[2]/a['+ str(j)+ ']').click()
    else:
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[3]/div[2]/a['+ str(j)+ ']').click()

    if (j>=10):
        break
    
    
import csv
with open('newdelhi1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(list1)