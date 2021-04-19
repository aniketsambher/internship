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
#PROXY = "23.23.23.23:3128"
#chrome_options = WebDriver.ChromeOptions()
#options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument('headless')
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--proxy-server=")

driver = webdriver.Chrome(options=options)
driver.get('https://www.99acres.com/')
driver.implicitly_wait(100)

driver.find_element_by_xpath('//*[@id="keyword"]').send_keys('delhi')
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="keyword"]').send_keys(Keys.ENTER)

driver.implicitly_wait(2)
#//*[@id="srp_tuple_price"]
driver.maximize_window()
p=driver.current_window_handle
a=[]
for j in range(2,20):
    for i in range(1,20):
        try:
            driver.find_element_by_xpath('(//*[@id="srp_tuple_property_title"]/h2)['+str(i)+']').click()
        except:
            continue
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(2)
        #we have either super build up area,plot area area moreover it can be given in sq ft or sq m
        #first setting area in sq feet
        try:
            driver.find_element_by_xpath('//*[@id="factArea"]/a/span').click()
            driver.find_element_by_xpath('//*[@id="factArea"]/a/ul/li[1]').click()
        except:
            driver.close()
            driver.switch_to.window(p)
            continue


        try:
            area=driver.find_element_by_xpath('//*[@id="superbuiltupArea_span"]').text
        except: 
            pass   
        try:
            area=driver.find_element_by_xpath('//*[@id="builtupArea_span"]').text
        except: 
            pass
        try:
            area=driver.find_element_by_xpath('//*[@id="carpetArea_span"]').text
        except: 
            pass
        try:
            area=driver.find_element_by_xpath('//*[@id="superArea_span"]').text
        except: 
            pass
        ######################
        try:
            price=driver.find_element_by_xpath('//*[@id="pdPrice2"]').text
            if(price.split(' ')[1]=='Cr' or price.split(' ')[1]=='Crore'):
                price=int(price.split(' ')[0])*100
            else:
                price=int(price.split(' ')[0])

        except:
            price=-1
        try:
            floor=driver.find_element_by_xpath('//*[@id="floorNumLabel"]').text[0]
        except:
            floor=-1
        try:
            propertyage=driver.find_element_by_xpath('//*[@id="agePossessionLbl"]').text.text.split(' ')[0]
        except:
            propertyage=-1
        try:
            facing=driver.find_element_by_xpath('//*[@id="facingLabel"]').text.split('-')[0]
        except:
            facing=-1
        try:
            bedrooms=driver.find_element_by_xpath('//*[@id="bedRoomNum"]').text[0]
        except:
            bedrooms=-1
        try:
            bathrooms=driver.find_element_by_xpath('//*[@id="bathroomNum"]').text[0]
        except:
            bathrooms=-1
        try:
            balconies=driver.find_element_by_xpath('//*[@id="balconyNum"]').text[c]
        except:
            balconies=-1
        try:
            address=driver.find_element_by_xpath('//*[@id="FactTableComponent"]/tr[2]/td[2]/div[2]').text
        except:
            pass
        a.append([area,price,floor,propertyage,facing,bedrooms,bathrooms,balconies,address])
        print(a)
        driver.close()
        driver.switch_to.window(p)
    driver.switch_to.window(p)
    print(driver.current_window_handle)
    driver.implicitly_wait(2)
    #<a href="https://www.99acres.com/property-in-delhi-ncr-ffid-page-2" class="">2</a>
    #'//[@href='https://www.99acres.com/property-in-delhi-ncr-ffid-page-2']'
    #"//a[@href='/docs/configuration']")).click();
    #driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[4]/div[1]').click()
    
    driver.get('https://www.99acres.com/property-in-delhi-ncr-ffid-page-'+str(j))
    
    #'//*[@id="app"]/div/div/div[2]/div[2]/div[3]/div[2]/a['+ str(j)+ ']'
    
