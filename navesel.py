from asyncio import exceptions
from site import venv
from tokenize import Special
from selenium import webdriver 
import selenium 
from time import sleep 
import pandas as pd
import time  
import requests
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="/home/zec/Desktop/Selenium/geckodriver") 
driver.get("https://www.navexpo.com/en/exhibitors/exhibitors-2021/item/carlier-chaines") 
time.sleep(5)

#click on ok button
driver.find_element(By.CLASS_NAME, 'button_custom.btn_ok').click()
time.sleep(3)
name=[]
website=[]
phone=[]
Special=[]

try:
    while(True):
        
        try:
            #names
            rayr=driver.find_element(By.TAG_NAME, 'h1').text
            print(rayr)
            name.append(rayr)
        except:
            name.append(None) 

        try:
            #website
            jyt=driver.find_element(By.CLASS_NAME,'element.element-link')
            spi=jyt.find_element(By.TAG_NAME,'a').text
            print(spi)
            time.sleep(2)
            website.append(spi)
        except:
            website.append(0)

        try:
            #phone number
            ii=driver.find_element(By.CLASS_NAME,'element.element-text').text
            print(ii)
            time.sleep(2)
            phone.append(ii)
        #print(ii)
        except:
            phone.append(0) 
        try:
            kkl=driver.find_element(By.CLASS_NAME,'uk-margin.element.element-itemcategory').text
            print(kkl)
            time.sleep(2)
            Special.append(kkl)
        except:
            Special.append(0)

        




        xyz=driver.find_element(By.CLASS_NAME,'page-nav.clearfix')

        ff=xyz.find_element(By.LINK_TEXT,'Next >')
        if ff:
            ff.click()
        else:
            break

except:

   print("job is done")

her = {

"NAME": name,
"WEBSITE":website,
"PHONE":phone,
"SPECIAL":Special
}
print(name)
print(website)
print(phone)
df = pd.DataFrame.from_dict(her, orient='index')
df = df.transpose()

df.to_csv("koo.csv")


