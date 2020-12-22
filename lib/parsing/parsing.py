from selenium import webdriver as wd
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import numpy as np
import time
from selenium.webdriver.common.keys import Keys 

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def game(x, y):
    #ua = dict(DesiredCapabilities.CHROME)
    options = wd.ChromeOptions()
    #options.add_argument('headless')
    options.add_argument("--window-size=1920,1080")
    driver = wd.Chrome(options=options)
    for ngame in range(x, y):
        driver.get("https://cs.fail/crash/history/"+str(ngame))
        driver.execute_script("document.body.style.zoom='zoom 80%'")
        time.sleep(0.2)
        point = driver.find_element_by_xpath('/html/body/app-root/app-wrapper/div/div/app-crash-game/div/div/div[3]/div/div/div/div/div[15]')#доходим до 15-го игрока
        point.click()
        time.sleep(0.2)
        allmoney = driver.find_elements_by_class_name("zbet__total")
        startmoney =sum([float(x.text) for x in allmoney])#сколько всего поставили денег
        elem2=driver.find_elements_by_class_name("zbet__price")
        lst2=[x.text for x in elem2]
        lst22=[float(x) for x in lst2 if is_number(x)]
        earn=startmoney-sum(lst22)#сколько сайт поднял
        email_in111 = driver.find_element_by_xpath('/html/body/app-root/app-wrapper/div/div/app-crash-game/div/div/div[2]/div[1]/div[3]/button/div')
        email_in111.click()
        time.sleep(2)
        email_in0 = driver.find_element_by_xpath('/html/body/app-root/app-wrapper/div/app-modals-container/app-modal/div/div/div/div[2]/div[2]/div[2]')
        coeff=float(email_in0.text)#коэффициент игры
        return ([coeff, earn, ngame])
    driver.quit()

game(742466,742468)