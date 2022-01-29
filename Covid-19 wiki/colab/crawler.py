from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

# 1. Thêm 1 số các cài đặt cho Chrome như ẩn  kích .
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

# 2. Khởi tạo một đối tượng browser.
browser = webdriver.Chrome(executable_path="./chromedriver")

# 3. Tạo url - change url by site.
pages = ['COVID-19','COVID-19 pandemic', 'COVID-19 vaccine', 'Severe acute respiratory syndrome coronavirus 2', 'COVID-19 misinformation', 'Social distancing', 'Transmission (medicine)',
         'Symptoms of COVID-19', 'COVID-19 testing', 'Workplace hazard controls for COVID-19', 'COVID-19 drug development', 'Economic impact of the COVID-19 pandemic']

covid_19 = []

for i in range(len(pages)):
    url = 'https://en.wikipedia.org/wiki/' + str(pages[i])
    browser.get(url)
    sleep(3)

    paras = browser.find_elements_by_tag_name('p')
    content = ""
    for para in paras:
        content += para.text
        content += '\n'
    covid_page = {
        "page": pages[i],
        "text": content,
        "link": url
    }
    covid_19.append(covid_page)

covid_19_df = pd.DataFrame(covid_19)
covid_19_df.to_csv('./covid19-wiki.csv', index=True)
sleep(2)
browser.close()