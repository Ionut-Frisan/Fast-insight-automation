from selenium import webdriver
from selenium.webdriver import ChromeOptions
import os

PATH = os.getcwd() + "\chromedriver.exe"

Chromeoptions = ChromeOptions()

Chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
Chromeoptions.add_argument("window-size=1280,800")

driver = webdriver.Chrome(PATH, options=Chromeoptions)
driver.get("https://mcdonalds.fast-insight.com/voc/ro/ro")