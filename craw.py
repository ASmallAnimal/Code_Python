from selenuim import selenuim
from selenuim import webdriver
from selenuim.commom.exeptions import NoSuchException
from selenuim.webdriver.commom.Keys import Keys
import time
from bs4 import BeautifulSoup

browser=webdriver.GoogleChrome('https://t.bilibili.com/348333886500733700?tab=2')
browser.get()
soup=BeautifulSoup(browser.page_sourse)
while len('')>0:
    a.neme.vip-red-name