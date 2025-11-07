import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import pandas as pd
from itertools import zip_longest

website = 'https://quotes.toscrape.com/'
path = r"D:\Maro\Scraping\Selenium\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
time.sleep(3)

Quote = []
Name = []
Tags = []
About = []

containers = driver.find_elements(By.CLASS_NAME, 'quote')
for cont in containers:
    quote_text = cont.find_element(By.CLASS_NAME, 'text').text
    author = cont.find_element(By.CLASS_NAME, 'author').text
    tag_elements = cont.find_elements(By.CLASS_NAME, 'tag')
    tags = [t.text for t in tag_elements]
    about = cont.find_element(By.TAG_NAME, 'a').get_attribute('href')

    print(f"Quote: {quote_text}")
    print(f"Author: {author}")
    print(f"Tags: {tags}")
    print(f"About: {about}")
    print("-" * 50)


    Quote.append(quote_text)
    Name.append(author)
    Tags.append(", ".join(tags))
    About.append(about)

driver.quit()

# Export to CSV
file_list = [Quote, Name, Tags, About]
exported = zip_longest(*file_list)

with open("Quotes to Scrape.csv", "w", encoding="utf-8", newline='') as myfile:
    writer = csv.writer(myfile)
    writer.writerow(['Quote', 'Name', 'Tags', 'About'])
    writer.writerows(exported)