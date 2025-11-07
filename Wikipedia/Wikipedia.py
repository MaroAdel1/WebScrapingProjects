import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import pandas as pd
from itertools import zip_longest

website = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
path = r"D:\Maro\Scraping\Selenium\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
time.sleep(3)

Country = []
GDP_2025 = []
GDP_2022 = []
GDP_2023 = []

table = driver.find_element(By.XPATH, "(//table[contains(@class,'wikitable')])[1]")
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) >= 4:  # تأكد أن الصف يحتوي على 4 أعمدة على الأقل
        country = cells[0].text.strip()
        gdb2025 = cells[1].text.strip()
        gdb2022 = cells[2].text.strip()
        gdb2023 = cells[3].text.strip()

        print(f"Country: {country}")
        print(f"GDP 2025: {gdb2025}")
        print(f"GDP 2022: {gdb2022}")
        print(f"GDP 2023: {gdb2023}")
        print("-" * 50)

        Country.append(country)
        GDP_2025.append(gdb2025)
        GDP_2022.append(gdb2022)
        GDP_2023.append(gdb2023)

driver.quit()

# Export to CSV
file_list = [Country, GDP_2025, GDP_2022, GDP_2023]
exported = zip_longest(*file_list)

with open("Wikipedia.csv", "w", encoding="utf-8", newline='') as myfile:
     writer = csv.writer(myfile)
     writer.writerow(['Country', 'GDP_2025', 'GDP_2022', 'GDP_2023'])
     writer.writerows(exported)