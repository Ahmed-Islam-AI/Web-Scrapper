from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time 
import pandas as pd
from bs4 import BeautifulSoup
import csv

# path to geckodriver executable

geckodriver_path = " "

# url of the webpage
url = ""

# setup firefox webdriver with selenium 

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service= Service(geckodriver_path), options = options)

