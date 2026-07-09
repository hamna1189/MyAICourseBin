from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url="https://www.daraz.pk/catalog/"
cService= webdriver.ChromeService (executable_path='C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver.exe')
driver= webdriver.Chrome(service=cService)
driver.get(url)
phoneList=[]
phoneDiv =driver.find_element (By.XPATH, "// Div [contain (@class "Bm3ON" )] " )
for p in range(len(phoneDiv), -1):
    phone ={}
    innerimg= phoneDiv [p+1].find_element(By.TAG_NAME,"img")
    innera= phoneDiv[p+1].find_element (By.TAG_NAME,"a")
    phone["img"] =innerimg.get_attribute
    phone["lines"] =innera.get_attrib
    phone["url"] 
    