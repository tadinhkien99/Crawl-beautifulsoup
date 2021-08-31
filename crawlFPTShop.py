import time
import pandas as pd
from httpx import TimeoutException
from scrapy.http import HtmlResponse
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("--headless")
link_web = "https://www.nguyenkim.com/dien-thoai-di-dong/"


def crawl_data_in_page(link):
    category = {'name': [], 'price': [], 'img_src': []}
    # response = requests.get(link).text
    driver = webdriver.Chrome(r"C:\Users\DELL\Downloads\chromedriver\chromedriver.exe", options=options)
    driver.get(link)

    # time.sleep(2)
    for i in range(2):
        time.sleep(0.5)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(5)
        response = driver.page_source

        soup = BeautifulSoup(response, "html.parser").contents
        dom = etree.HTML(str(soup))
        name = dom.xpath("//*[@class='item-list product']/div[2]/div[2]/a/text()")
        price = dom.xpath("//*[@class='item-list product']/div[2]/div[3]/p[1]/text()")
        img = dom.xpath("//*[@class='item-list product']/div[1]/div[1]/a/div/img/@src")
        print(img)
        category['name'].extend(name)
        category['price'].extend(price)
        category['img_src'].extend(img)
        # print(category)
        # for phone in src:
        #     print(phone)
        try:
            if driver.find_element_by_xpath("//*[@class='btn_next ty-pagination__item ty-pagination__btn ty-pagination__next cm-history ']"):
                driver.find_element_by_xpath("//*[@class='btn_next ty-pagination__item ty-pagination__btn ty-pagination__next cm-history ']").click()
            else:
                # print(category)
                break
        except:
            pass
        return category
#             //*[@id="102351"]/div[2]/div[2]/a
#               //*[@id="103875"]/div[1]/div[2]/div[2]/a
# //*[@id="104295"]/div[1]/div[1]/div[1]/a/div/img
# //*[@id="104295"]/div[1]/div[2]/div[2]/a
# //*[@id="104295"]/div[1]/div[2]/div[3]/p[1]

# def crawl_page():
#     for

categories = crawl_data_in_page(link_web)
# df = pd.DataFrame(categories)
# print(df)
# writer = pd.ExcelWriter('./phone_store.xlsx')
# df.to_excel(writer,'Sheet1', index=None)
# writer.save()
