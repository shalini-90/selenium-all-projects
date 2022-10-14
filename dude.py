#VkpGBb 
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

name=[]
address=[]
phone=[] 
reu=driver.find_elements(By.CLASS_NAME,'VkpGBb')

#for i in reu:
# 
# 

def next_click():
    
    try:
        em = driver.find_element(By.LINK_TEXT, 'Next')
        em.click()
        time.sleep(6)
        scrap()
    except:
        print('job is done')

       
def scrap():
    reu=driver.find_elements(By.CLASS_NAME,'VkpGBb')

    for i in reu: 
        # x=[]
        #name
        i.find_element(By.CLASS_NAME,'dbg0pd.eDIkBe').click() 
        time.sleep(5) 

        try:
            uu=driver.find_element(By.CLASS_NAME, 'qrShPb.kno-ecr-pt.PZPZlf.q8U8x.PPT5v').text 
            name.append(uu)
            print(uu)
        except:
            name.append(None) 

    
        
        try:
            gdfg=driver.find_element(By.CLASS_NAME,'LrzXr').text 
            address.append(gdfg)
            print(gdfg)
        except:
            address.append("NaN")
            print(gdfg)

        try: 
            

            jyt=driver.find_element(By.CLASS_NAME,'LrzXr.zdqRlf.kno-fv')
            spi=jyt.find_elements(By.TAG_NAME,'span')
            phone.append(spi[1].text)

        except:
            phone.append(0) 
            print(phone)  
            
    next_click()
        
scrap()



          
kjoo = {
    
    "NAME": name,
   "ADDRESS":address,
    "PHONE":phone

}
    
  

df = pd.DataFrame.from_dict(kjoo, orient='index')
df = df.transpose()

df.to_csv("kkk.csv")
  

        #YyVfkd
