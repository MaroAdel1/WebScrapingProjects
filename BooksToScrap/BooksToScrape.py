import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import pandas as pd
from itertools import zip_longest

BookName = []
Price = []
Rating = []
In_Out_stock = []

page_num: int = 1
total_pages = 50
while page_num <= total_pages:
         try:
            website = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
            path = r"D:\Maro\Scraping\Selenium\chromedriver-win64\chromedriver.exe"
            service = Service(executable_path=path)
            driver = webdriver.Chrome(service=service)
            driver.get(website)
            # time.sleep(3)

            containers = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')
            for cont in containers:
                bookname = cont.find_element(By.TAG_NAME, 'h3').find_element(By.TAG_NAME, 'a').get_attribute('title')
                price = cont.find_element(By.CLASS_NAME, 'price_color').text.strip()
                rating = cont.find_element(By.CSS_SELECTOR, 'p.star-rating').get_attribute('class').replace('star-rating ', '')
                stock = cont.find_element(By.CSS_SELECTOR, 'p.instock.availability').text.strip()

                BookName.append(bookname)
                Price.append(price)
                Rating.append(rating)
                In_Out_stock.append(stock)

            driver.quit()
            page_num += 1
         except Exception as e:
                print("Error occurred on page", page_num, ":", e)
                break

# Export to CSV
file_list = [BookName, Price, In_Out_stock,Rating]
exported = zip_longest(*file_list)

with open("Books To Scrape.csv", "w", encoding="utf-8", newline='') as myfile:
     writer = csv.writer(myfile)
     writer.writerow(['BookName', 'Price', 'In_Out_stock', 'Rating'])
     writer.writerows(exported)