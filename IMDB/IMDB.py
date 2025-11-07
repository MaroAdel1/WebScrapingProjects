import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import pandas as pd
from itertools import zip_longest

website = 'https://www.imdb.com/chart/top/'
path = r"D:\Maro\Scraping\Selenium\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
time.sleep(3)

Name = []
Year = []
Rating = []
Links = []

containers = driver.find_elements(By.XPATH, "//li[@class='ipc-metadata-list-summary-item']")
for cont in containers:
    name = cont.find_element(By.XPATH, ".//h3").text
    year = cont.find_element(By.XPATH, ".//div[contains(@class,'cli-title-metadata')]/span[1]").text
    rating = cont.find_element(By.XPATH, ".//span[contains(@class,'ipc-rating-star--rating')]").text
    link = cont.find_element(By.TAG_NAME, 'a').get_attribute('href')
    print(f"name: {name}")
    print(f"year: {year}")
    print(f"rating: {rating}")
    print(f"link: {link}")
    print("-" * 50)


    Name.append(name)
    Year.append(year)
    Rating.append(rating)
    Links.append(link)

driver.quit()

# Export to CSV
file_list = [Name, Year, Rating, Links]
exported = zip_longest(*file_list)

with open("IMDB.csv", "w", encoding="utf-8", newline='') as myfile:
    writer = csv.writer(myfile)
    writer.writerow(['Name', 'Year', 'Rating', 'Links'])
    writer.writerows(exported)