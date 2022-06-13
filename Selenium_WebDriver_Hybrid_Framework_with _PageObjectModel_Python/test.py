from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C:/Users/dips2/Documents/Dipanjana/Preperation/Testing/selenium/drivers/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url='https://www.google.com'
browser.get(url)