import os
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get('https://www.vestnesis.lv/oficialie-pazinojumi/izsoles')
driver.find_element_by_name('fname')

time.sleep(1)
myinput=driver.find_element_by_name('fname')
myinput.send_keys('rīga dzīvokļa īpašums')
time.sleep(1)
myclick=driver.find_element_by_class_name('helper')
myclick.click()
time.sleep(1)
visi_linki=driver.find_elements_by_class_name('article')
for elem in visi_linki:
    e=elem.get_attribute("href")
    print(e)
driver.close()