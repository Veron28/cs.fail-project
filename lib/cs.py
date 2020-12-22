from selenium import webdriver as wd
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def game(x, y):
    ua = dict(DesiredCapabilities.CHROME)
    options = wd.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x935')
    driver = wd.Chrome(options=options)
    for ngame in range(x, y):
        driver.get("https://cs.fail/crash/history/"+str(ngame))
        time.sleep(0.2)
        try:
            allmoney = driver.find_elements_by_class_name("zbet__total") #сколько деняк ставили первые 15
            startmoney =sum([float(x.text) for x in allmoney])#сколько всего поставили денег
            elem2=driver.find_elements_by_class_name("zbet__price")
            lst2=[x.text for x in elem2]
            lst22=[float(x) for x in lst2 if is_number(x)]
            earn=startmoney-sum(lst22)#сколько сайт поднял
            email_in111 = driver.find_element_by_class_name('xbutton__text')
            email_in111.click()
            time.sleep(0.1)
            email_in0 = driver.find_element_by_xpath('/html/body/app-root/app-wrapper/div/app-modals-container/app-modal/div/div/div/div[2]/div[2]/div[2]')
            coeff=float(email_in0.text)#коэффициент игры
            yield ([coeff, earn, ngame])
        except Exception:
            yield ('Stop')
            break
    driver.quit()

start_time = time.time()
gm = game(728780, 728790)
for i in gm:
    print(i)

print("--- %s seconds ---" % (time.time() - start_time))
