from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get('http://demo:Test@123@test.bookingclap.com/en/index.html')

inputElems=driver.find_element_by_xpath('//*[@id="home"]/form/div[1]/div/div[1]/div[1]/input[2]').send_keys('london')
time.sleep(3)

for inputElem in inputElems:

    inputElem.send_keys('Search strings...')

    inputElem.send_keys(keys.ENTER)