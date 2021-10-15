# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='/home/ymizushi/Develop/sandbox/python/selenium/chromedriver')
driver.get("https://www.yahoo.co.jp/")
time.sleep(1)
driver.close()
