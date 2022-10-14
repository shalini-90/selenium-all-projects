from selenium import webdriver 
import selenium 
from time import sleep 
import pandas as pd
import time  
import requests
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="/home/zec/Desktop/Selenium/geckodriver") 
driver.get("https://www.google.com/") 
x= "programming coaching in indore"
y=driver.find_element(By.CLASS_NAME,'gLFyf.gsfi').send_keys(x)  
time.sleep(2)
driver.find_element(By.CLASS_NAME,'gNO89b').click() 
time.sleep(3)
    # driver.execute_script('scrollTo(0,300)') 
    # time.sleep(2) 
    #k="More places" 
    #z=driver.find_element(By.CLASS_NAME,'MXl0lf tKtwEb wHYlTd').click() 
driver.find_element(By.CLASS_NAME,'wUrVib.OSrXXb').click() 
time.sleep(2)  
reu=driver.find_elements(By.CLASS_NAME,'VkpGBb').click()

name=[] 
address=[]
phone=[]

def next_click():
    try:
        driver.find_element(By.LINK_TEXT, 'Next').click()
        time.sleep(2)
        scrap() 
    except:
        print(0) 

def scrap():
    reu=driver.find_elements(By.CLASS_NAME,'VkpGBb') 
    for i in reu:
        i.click()
        time.sleep(3)

    try:
           # trr=i.find_element(By.CLASS_NAME,'OSrXXb').click() 
       # time.sleep(2) 
        uu=driver.find_element(By.CLASS_NAME,'SPZz6b').text 

        name.append(uu) 

    except:
        name.append(0) 

    try:

        gdfg=driver.find_element(By.CLASS_NAME,'LrzXr').text 
        address.append(gdfg)
    except:
        address.append(0)
    # print(gdfg) 

    try: 
            # LrzXr zdqRlf kno-fv

            jyt=driver.find_element(By.CLASS_NAME,'LrzXr.zdqRlf.kno-fv')
            spi=jyt.find_elements(By.TAG_NAME,'span')
            phone.append(spi[1].text)

    except:
        phone.append(0) 

        kjoo = {
    
    "NAME": name,
    "ADDRESS":address,
    "PHONE":phone
    
}   

    df = pd.DataFrame.from_dict(kjoo, orient='index')
    df = df.transpose()

    df.to_csv("kjoo.csv")