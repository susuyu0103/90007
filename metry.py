#11/23 動態網頁 ettoday
import csv
import requests
import pandas as pf
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time,datetime

from time import sleep
import sys

#==============================================================================

url='https://www.ettoday.net/news/news-list-2020-12-12-0.htm'

options = webdriver.ChromeOptions()                             #新增,掠過網頁憑證錯誤
options.add_argument('--ignore-certificate-errors')            #新增,掠過網頁憑證錯誤
#options.add_argument('user-agent-{}'.format(headers))        #新增,掠過網頁憑證錯誤
driver = webdriver.Chrome(chrome_options=options)             #新增,掠過網頁憑證錯誤   

driver.get(url)
page=0

with open('google_search3333.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('時間','標題','概述'))
    writer.writerow(['連結'])


    now_date = time.strftime("%Y%m%d")
    day=int(now_date[-2:])


    n_days1=5  #要幾天

    for i in range(0,n_days1):
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=i)
        n_days = now-delta
        now1=now.strftime('%Y%m%d')
        
        print (now1)
        n_days1=n_days.strftime('%Y%m%d')
        print (n_days1)
        print(i,'天前','月份',n_days1[-4:-2],'日期',n_days1[-2:])
        # =============================抓網頁======================================
        # def test_app_dynamics_job(self):
        # driver = self.driver
        # driver.get("https://www.ettoday.net/news/news-list.htm")
        # driver.find_element_by_xpath("//div[4]/div").click()
        driver.find_element_by_id("selY").click()
        Select(driver.find_element_by_id("selY")).select_by_visible_text("2020")
        driver.find_element_by_id("selY").click()
        driver.find_element_by_id("selM").click()
        Select(driver.find_element_by_id("selM")).select_by_visible_text(n_days1[-4:-2])
        driver.find_element_by_id("selM").click()
        driver.find_element_by_id("selD").click()
        Select(driver.find_element_by_id("selD")).select_by_visible_text(str(int(n_days1[-2:])))
        driver.find_element_by_id("selD").click()
        
        driver.find_element_by_id("button").click()
    
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_span= sp.select(" div.part_list_2 > h3 >span")
        search_em = sp.select(" div.part_list_2 > h3 > em")
        search_href = sp.select(" div.part_list_2 > h3 > a")
        
        for i in range(len(search_span)):#len(search_span)
                print(page)
                print(search_span[i].text)
                print(search_em[i].text)
                print(search_href[i].text)
                print(search_href[i].get('href'))
        
                writer.writerow([search_span[i].text , search_em[i].text , search_href[i].text])
                writer.writerow([search_href[i].get('href')])
    
        # driver.find_element_by_xpath("//a[@id='pnnext']/span[2]").click()
        
        sleep(1)  # 必須加入等待，否則會有誤動作



#     for i in range(8):
#         page+ = 1
#         html = driver.page_source
#       sp=BeautifulSoup(html,"html.parser")
#       search_h3=sp.select("div.yuRUbf > a > h3")
#       search_a=sp.select("div.yuRUbf > a")
#       search_span=sp.select("div.IsZvec > div > span.aCOpRe")

