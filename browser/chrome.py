import random
import selenium
import pyautogui
from time import sleep
from seleniumwire import webdriver
from random import uniform, randint
from selenium.webdriver.common.by import By
# from config import login, password, ip, user_agent
from webdriver_manager.chrome import ChromeDriverManager


# основные значения для коректного запуска
users = []
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False
# открытие текстового файла
lines = open('text1.txt').read().splitlines()
# драйвер для chrome
driver_one = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
        )

class Script:
    '''Создание, запуск браузера и автоматизация'''
    def browser(self, width):
        # размер и положение открытого окна
        driver_one.set_window_size(480, 900)
        driver_one.set_window_position(width, 0)
        # запуск браузера
        driver_one.get(url='https://web.whatsapp.com/')
        sleep(5)
        input('Введите что-нибудь после сканирования QR-кода: ')
    def auto(self):
        # фильтр непрочитанных сообщений
        filter_one = driver_one.find_element(By.CLASS_NAME, 'p357zi0d.ktfrpxia.nu7pwgvd.ac2vgrno.sap93d0t.gndfcl4n.ekdr8vow.dhq51u3o.s4k44ver.g9p5wyxn.i0tg5vk9.aoogvgrq.o2zu3hjb')
        while True:
            try:
                filter_one.click()
                users = driver_one.find_elements(By.CLASS_NAME, 'l7jjieqr.il1gyv3w.ei5e7seu.h0viaqh7.tpmajp1w.k07a8sro.riy2oczp.dsh4tgtl.hnx8ox4h.gz7w46tb.lyutrhe2.qfejxiq4.fewfhwl7.ovhn1urg.ap18qm3b.ikwl5qvt.j90th5db.aumms1qt')
                # отправка сообщений
                pyautogui.moveTo(randint(1, 900), randint(1, 900), duration=uniform(0.2, 0.7))
                sleep(2)
                # отправка ответов по новым сообщениям
                for user in users:
                    user.click()
                    pyautogui.moveTo(randint(1, 900), randint(1, 900), duration=uniform(0.2, 0.7))
                    sleep(0.5)
                    # клик по написанию
                    driver_one.find_element(By.XPATH, '//div[@class="p3_M1"]')
                    sleep(0.5)
                    # написание с помощью клавиатуры
                    pyautogui.write(random.choice(lines), interval = uniform(0.1, 0.2))
                    sleep(0.5)
                    # кнопка отправки сообщения
                    driver_one.find_element(By.CLASS_NAME, '_3HQNh._1Ae7k').click()
                    sleep(1)
                    filter_one.click()
                    sleep(1)
            # ошибка ненахождения новых элементов    
            except selenium.common.exceptions.StaleElementReferenceException as ex:
                pass
                print(ex)
                print('Пользователи не найдены')
            # закрытие браузера при другой ошибке
            finally:
                print('ERROR')
# обозначение класса
bro = Script()


def one_browser():
    bro.browser(0)
    while True:
        bro.auto()