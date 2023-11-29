from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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


def open_page(model: str) -> str:
    "функция получает название модели и возвращает url с описанием этой модели на сайте производителя"
    print("открываю урл")
    driver.get(url)
    time.sleep(1)
    driver.implicitly_wait(3)
    search = driver.find_element(By.XPATH, '//*[@id="div_TopRightNarrow"]/div[1]/div[1]/input')
    search.click()
    search.click()
    search.send_keys(model)
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(7)
    good_url = driver.current_url
    return good_url


def get_proc():
    "временная функция, парсит страницу по ссылке и записывает нужные данные в файл"
    driver.get("https://psref.lenovo.com/Detail/IdeaPad_Slim_3_15IRU8?M=82X70045RK")
    driver.implicitly_wait(3)
    try:
        # proc = driver.find_element(By.XPATH, '//*[@id="as_SpecData"]/tbody[1]/tr[2]/td[2]/div/text()')
        proc = driver.find_element(By.XPATH, '//*[@id="as_SpecData"]')
        data = proc.text
        with open("table_good.txt", 'w', encoding='utf-8') as file:
            "обнуляем файл"
            file.write('')
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


def get_good_data(model: str) -> None:
    "парсит страницу по ссылке и записывает нужные данные в файл"
    driver.get(open_page(model))
    driver.implicitly_wait(7)
    time.sleep(5)
    try:
        # proc = driver.find_element(By.XPATH, '//*[@id="as_SpecData"]/tbody[1]/tr[2]/td[2]/div/text()')
        proc = driver.find_element(By.XPATH, '//*[@id="as_SpecData"]')
        data = proc.text
        with open("table_good.txt", 'w', encoding='utf-8') as file:
            "обнуляем файл"
            file.write('')
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

def test_parcing(url: str):
    "функция для тестовых парсингов"
    driver.get(url)
    table = driver.find_element(By.XPATH, '//*[@id="product-tabs-0"]/div/div[2]')
    print(table.text)
    with open('test_parcing.txt', 'w', encoding='utf-8') as file0:
        file0.write('')
    for i in table.text:
        with open('test_parcing.txt', 'a', encoding='utf-8') as file:
            file.write(i)
    time.sleep(66)

def index_txt_file():
    """функция проходится построчно по файлу и создает такой же файл, но с индексом строчки в начале
    это нужно просто для личного удобства"""
    with open('index_test_parcing.txt', 'w', encoding='utf-8') as file0:
        file0.write('')
    with open('test_parcing.txt', 'r', encoding='utf-8') as file0:
        with open('index_test_parcing.txt', 'a', encoding='utf-8') as file:
            i = 0
            while True:
                tmp_string = file0.readline()
                print('tmp_string = ', tmp_string)
                if tmp_string == '':
                    break
                print(i, tmp_string)
                file.write('[' + str(i) + '] ' + str(tmp_string) + '\n')
                # file.write(str('[' + str[i] + ']' + '\n'))
                i += 1



test_url = 'https://neon-night.ru/product/girlyanda-aysikl-bakhroma-svetodiodnyy-4-8-kh-0-6-m-belyy-provod-230-v-diody-teplyy-belyy-152-led/?ysclid=lpgkqtoq4d846110551'


# test_parcing(test_url)
index_txt_file()

# get_good_data('82X70045RK')
# get_good_data('21C10000UE')
# open_page('82X70045RK')
# open_page('21C10000UE')

# driver.get(url)
# driver.implicitly_wait(7)
# time.sleep(55)
