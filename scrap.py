from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
URL="https://www.amway.in/shop/c/nutrition"
browser = webdriver.Chrome("C:/Users/subhr/Downloads/Web scrapping/chromedriver.exe")
browser.get(URL)
time.sleep(10)
product=[]
def scrape():
    for i in range(1,10):
        print(f"scrapping page{i+1}.....")
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for div_tag in soup.find_all("div",attrs={'class':'productMetaData__details'}):
            h1_tags = div_tag.find_all("h1")
            temp_list = []
            for h1_tag in enumerate(h1_tags):
                try:
                    temp_list.append(h1_tag.contents[0])
                except:
                    temp_list.append("")
            product.append(temp_list)
        browser.find_element(by=By.XPATH,value='//*[@id="__next"]/div/div[2]/div/div/div[2]/div[2]/div[3]/div/div/svg/g/path').click()
scrape()
p=pd.DataFrame(product,columns=["Name"])
p.to_csv("product.csv")              
                