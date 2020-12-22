# -*- coding: utf-8 -*-

from selenium import webdriver as wd
from lib.last_game import is_number, game
import csv
import time
import pandas as pd
from itertools import chain
import numpy as np
import pickle

class Main_logic():


    def __init__(self):



        self.options = wd.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument("--window-size=1920,1080")
        self.driver = wd.Chrome(options=self.options)

        self.past_columns = [f"past_{i}" for i in range(98)]



    def load_last_game(self):

        self.driver.get("https://cs.fail/")
        time.sleep(0.5)

        try:

            self.ngame = int(str(self.driver.find_element_by_xpath(
                '/html/body/app-root/app-wrapper/div/div[1]/div/app-crash-sidebar/div[2]/div/div/a[1]').get_attribute(
                'href')).split('/')[-1])

        except Exception:

            self.driver.get("https://cs.fail/")
            time.sleep(1)
            self.ngame = int(str(self.driver.find_element_by_xpath(
                '/html/body/app-root/app-wrapper/div/div[1]/div/app-crash-sidebar/div[2]/div/div/a[1]').get_attribute(
                'href')).split('/')[-1])

        df = pd.read_csv("lib/start.csv", sep=',')
        listt = [int(i[0]) for i in df[['game']].to_numpy()]



        if listt[-1] + 50 > self.ngame:
            count = True
            i = listt[-1]
            flag = abs(self.ngame - listt[-1] - 50)
        else:
            with open("lib/start.csv", mode="w", encoding='utf-8') as a_file:
                file_writer = csv.writer(a_file, delimiter=",", lineterminator="\r")
                file_writer.writerow(['game', 'crash', 'bank'])
            count = True
            flag = 0
            i = self.ngame - 50
        while True:
            self.driver.get("https://cs.fail/crash/history/" + str(i))
            self.driver.execute_script("document.body.style.zoom='zoom 80%'")
            time.sleep(0.5)
            try:
                if count:  # Убираем чатик который нам не нужен (всплывает только при открытии первой ссылки)
                    chat = self.driver.find_element_by_xpath(
                        '/html/body/app-root/app-wrapper/div/div[2]/app-chat/div/div[1]/button')
                    chat.click()
                    count = False
                    time.sleep(0.2)
                point = self.driver.find_element_by_xpath(
                    '/html/body/app-root/app-wrapper/div/div[2]/div/app-crash-game/div/div/div[3]/div/div/div/div/div[15]')  # доходим до 15-го игрока
                point.click()
                time.sleep(0.5)
                allmoney = self.driver.find_elements_by_class_name("zbet__total")
                startmoney = sum([float(x.text) for x in allmoney])  # сколько всего поставили денег
                elem2 = self.driver.find_elements_by_class_name("zbet__price")
                lst2 = [x.text for x in elem2]
                lst22 = [float(x) for x in lst2 if is_number(x)]
                earn = round(startmoney - sum(lst22), 2)  # сколько сайт поднял
                email_in111 = self.driver.find_element_by_xpath(
                    '/html/body/app-root/app-wrapper/div/div[2]/div/app-crash-game/div/div/div[2]/div[1]/div[3]/button')
                email_in111.click()
                time.sleep(0.5)
                email_in0 = self.driver.find_element_by_xpath(
                    '/html/body/app-root/app-wrapper/app-modals-container/app-modal/div/div/div/div[2]/div[2]/div[2]')
                coeff = float(email_in0.text)  # коэффициент игры
                i += 1
                yield [i - 1, coeff, earn]

                if flag >= 50:
                    df = pd.read_csv("lib/start.csv")
                    df1 = np.transpose(df[-49:][['crash', 'bank']].to_numpy())
                    df2 = list(chain.from_iterable(list(zip(df1[0], df1[1]))))
                    df_ans = pd.DataFrame([df2], columns=self.past_columns)
                    loaded_model = pickle.load(open('lib/finalized_model11.sav', 'rb'))

                    yield [np.clip(loaded_model.predict(df_ans)[0] - 0.5, 1., 2.)]

                flag += 1

                with open("lib/start.csv", mode="a", encoding='utf-8') as a_file:
                    file_writer = csv.writer(a_file, delimiter=",", lineterminator="\r")
                    file_writer.writerow([i - 1, np.clip(coeff, 1., 2.), earn])
            except Exception as err:
                pass

        self.driver.quit()

# obj = Main_logic()
# for i in obj.load_last_game():
#     print(i)