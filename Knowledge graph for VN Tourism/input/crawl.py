from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# 1. Thêm 1 số các cài đặt cho Chrome như ẩn  kích .
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

# 2. Khởi tạo một đối tượng browser.
browser = webdriver.Chrome(executable_path="chromedriver")

# 3. Tạo url - change url by site.
url = "https://guide.cmego.com/guide-to-con-dao-islands/"
browser.get(url)
sleep(3)

paras = browser.find_elements_by_tag_name('p')
content = ""
for para in paras:
    content += para.text
    content += '\n'

# 4. Tìm kiếm nội dung.

with open("../dataset/vn_tourism.txt", 'a') as file:
    file.write(content)

file.close()

sleep(2)
browser.close()


