from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
url="https://www.amazon.com/"
cService = webdriver.ChromeService ( executable_path='C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)
driver.get(url)
qouestList =[]
qouestDiv =driver.find_element (By.XPATH," // div[contain(@class ,"a carour sel-card ucw-widget-carousl-element")]"
for item in qouestDiv :
    quote = {}
    innerImage =qouestDiv[p+1] .find_elements(By _TAG_NAME,"img")
    innera[p+1].find_element (By _TAG_NAME,"a")
    quote["img"]=InnerImg .get_attribute ('src')
    quote["lines"] =innerImage .get_attribute('alt') 
    quote["url"] = innera.get_attribute('href')
    qouestList.append(quote)

filename = "data.csv"
with open (filename, 'w'newline = '' ) as f :
    w = csv.DictWriter (f, ['url','img','lines','authors'] )
    w.writeheader() 
    for qouest in qouestList:
        w.writerow(quote)
driver.close()