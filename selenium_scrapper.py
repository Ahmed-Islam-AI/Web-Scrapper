from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time 
import pandas as pd
from bs4 import BeautifulSoup
import csv

# path to geckodriver executable

geckodriver_path = "C:/geckodriver.exe"

# url of the webpage
url = "https://www.daraz.pk/#?"

# setup firefox webdriver with selenium 

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service= Service(geckodriver_path), options = options)

driver.get(url)


search = driver.find_element(By.CLASS_NAME, "search-box__input--O34g")

search.send_keys("Mobile Phones")

driver.find_element(By.CLASS_NAME, "search-box__button--1oH7").click()

time.sleep(3)

# Access the fox of data
data = driver.find_elements(By.CLASS_NAME, "buTCk")

# print(len(data))
Name = []
Price = []
Discount = []
Sold = []
Rating = []
for item in data:
    try:
        name = item.find_element(By.CLASS_NAME, "RfADt").text.strip()
        Name.append(name)
    except:
        Name.append("")
        
    try:
        price = item.find_element(By.CLASS_NAME, "aBrP0").text.strip()
        Price.append(price)
        
    except:
        Price.append("")
        
    try:
        discount = item.find_element(By.CLASS_NAME, "WNoq3").text.strip()
        Discount.append(discount)
        
    except:
        Discount.append("")
    
    try:
        sold = item.find_element(By.CLASS_NAME, "_1cEkb").text.strip()
        Sold.append(sold)
        
    except:
        Sold.append("")
        
        
    try:
        rating = item.find_element(By.CLASS_NAME, "_1cEkb").text.strip()
        Rating.append(rating)
        
    except:
        Rating.append("")
        
        
        
# saving data in the csv file

pd.DataFrame({
    'Name': Name,
    "Price": Price,
    'Discount': Discount,
    'Sold': Sold,
    "Rating": Rating,
}).to_csv("daraz.csv", index =False)
        