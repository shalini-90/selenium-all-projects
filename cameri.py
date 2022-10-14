from site import venv
from selenium import webdriver 
import selenium 
from time import sleep 
import pandas as pd
import time  
import requests
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="/home/zec/Desktop/Selenium/geckodriver") 
driver.get("https://www.google.com/") 
x= "flipkart"
  
y=driver.find_element(By.CLASS_NAME,'gLFyf.gsfi').send_keys(x)  
time.sleep(2)

driver.find_element(By.CLASS_NAME,'gNO89b').click() 
time.sleep(2) 

driver.find_element(By.CLASS_NAME,'LC20lb.MBeuO.DKV0Md').click() 
time.sleep(2) 

# for removing login id and password pop up
driver.find_element(By.CLASS_NAME,'_2KpZ6l._2doB4z').click() 
time.sleep(2) 

z= "flipkart camera" 
# Searching box of flipkart to search
u=driver.find_element(By.CLASS_NAME,'_3704LK').send_keys(z) 
time.sleep(2) 

# Searching button of flipkart to click
driver.find_element(By.CLASS_NAME,'_34RNph').click() 
time.sleep(2) 
#NAME 
v=driver.find_element(By.CLASS_NAME,'_1YokD2 _3Mn1Gg')
time.sleep(2) 
print(v) 
#PRICE
dy=driver.find_element(By.CLASS_NAME,'_30jeq3._1_WHN1').text 
print(dy) 
#RATING 
ii=driver.find_element(By.CLASS_NAME,'_3LWZlK').text 
print(ii) 
ou=driver.find_element(By.CLASS_NAME,'rgWa7D').text
print(ou) 
#wa=driver.find_element(By.CLASS_NAME,'') 
name=[]
price=[]
rating=[] 
specifications=[]

def scrap(): 
    # Whole div
    ghee=driver.find_elements(By.CLASS_NAME,'_2kHMtA') 
    for i in ghee: 
        #NAME
        see=i.find_element(By.CLASS_NAME,'_4rR01T').text 
        name.append(see)
        time.sleep(2) 
        #PRICE
        dy=driver.find_element(By.CLASS_NAME,'_30jeq3._1_WHN1').text 
        price.append(dy)
        print(dy) 
        #RATING 
        ii=driver.find_element(By.CLASS_NAME,'_3LWZlK').text 
        rating.append(ii) 
        print(ii) 
        # SPECIFICATIONS
        ou=driver.find_element(By.CLASS_NAME,'rgWa7D').text 
        specifications.append(ou)
        print(ou)  

        scrap() 

her = {
    
    "NAME": name,
   "PRICE":price,
    "RATING":rating, 
    "SPECIFICATIONS":specifications

}
    
  

df = pd.DataFrame.from_dict(her, orient='index')
df = df.transpose()

df.to_csv("dictto.csv")

