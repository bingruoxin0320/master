#! /usr/bin/env/python
# —*— coding:utf-8 -*-

#
# import requests
#
#
# url = 'https://test-nativematerial.tt.cn/appnative/appcache'
# head = {"Server": "Apache-Coyote/1.1", "Content": "text/html;charset=UTF-8", "Transfer-Encoding": "chunked", "Date": "Mon, 25 May 2020 13:29:55 GMT"}
#
# t = requests.get(url)
# text = t.content.decode('utf8')
# print(text)


from selenium import webdriver
from time import *


url = 'http://test-media-hz.tt.cn'
quer = webdriver.Chrome()
b = quer.get(url)

def login():
    quer.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input').send_keys('nvmqyo72390@chacuo.net')
    quer.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div[1]/input').send_keys('q123456')
    sleep(20)
    # quer.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div[1]/div[1]/div/input')\
    #     .send_keys('')
    quer.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[4]/div/button/span').click()




login()



