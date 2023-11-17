from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import requests
import os
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# user agent
my_user_agent = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"
options.add_argument(f"user-agent={my_user_agent}")
driver = webdriver.Chrome(options=options)

url = 'https://psref.lenovo.com/'

def open_page(model):
    print("открываю урл")
    driver.get(url)
    time.sleep(1)
    driver.implicitly_wait(3)
    search = driver.find_element(By.XPATH, '//*[@id="div_TopRightNarrow"]/div[1]/div[1]/input')
    search.click()
    search.click()
    search.send_keys(model)
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(3)
    get_proc()

def get_proc():
    driver.get("https://psref.lenovo.com/Detail/IdeaPad_Slim_3_15IRU8?M=82X70045RK")
    driver.implicitly_wait(3)
    try:
        # proc = driver.find_element(By.XPATH, '//*[@id="as_SpecData"]/tbody[1]/tr[2]/td[2]/div/text()')
        proc = driver.find_element(By.XPATH, '//*[@id="as_SpecData"]')
        data = proc.text
        with open('table_good.txt', 'a', encoding='utf-8') as file:
            print('записываю файл')
            for i in data:
                file.write(i)
            print("файл записан")
        list_goods = []
        with open('table_good.txt', 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                list_goods.append(line)
        print(list)



    except Exception as ex:
        print(ex)

# driver.get(url)
# driver.implicitly_wait(7)
# time.sleep(55)