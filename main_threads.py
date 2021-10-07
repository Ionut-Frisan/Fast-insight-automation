from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions
import time
import random
import generate_code
import threading
import multiprocessing
import os

SCROLL_PAUSE_TIME = 0.5

Chromeoptions = ChromeOptions()
#Chromeoptions.add_argument("--incognito")

PATH = os.getcwd() + "\chromedriver.exe"

codes = generate_code.get_codes('0dfxrsypazsv', 500)
#print(codes)

runtimes = 0
finished = False

merite = ['Totul a fost ok', 'Minunat', 'de vis', 'excelent', 'a fost ok', 'angajati seriosi, manageri pertinenti',
          'per total a fost super', 'mancarea a fost foarte buna si proaspata', 'inghetata e excelenta',
          'am fost serviti foarte repede si comanda a fost intreaga', 'mediul este unul foarte placut',
          'mancarea e geniala!!!', 'puisor is life', 'kutgw', 'as recomanda cu drag', 'mirobolant',
          'Mi-a lasat o impresie foarte buna aceasta experienta', 'tineti-o tot asa!', '10/10', 'super super <3',
          'ofertele de pe aplicatie', 'Toti angajatii', 'echipa foarte frumoasa', 'mancare proaspata',
          'atmosfera placuta', 'amabilitate', 'zambetele se vad si prin masti :)', 'servirea rapida',
          'rapiditate si mancare buna', 'asd', '.', 'tot', 'totul', 'curatenia',
          'mediul este placut si angajatii isi fac treaba foarte bine',
          'am avut o problema pe aplicatie,dar m-a ajutat un manager.Foarte seriosi si pregatiti']



#proxies = ['193.56.255.131','31.14.49.1','193.239.86.248','89.47.120.66','193.56.255.179','193.56.255.181','193.239.86.137','193.239.86.249','193.56.255.180','86.123.166.109','89.238.255.34']

def run(cod):
    global runtimes
    global finished
    global Chromeoptions
    global merite
    global PATH
    try:

        Chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
        Chromeoptions.add_argument("window-size=1280,800")

        driver = webdriver.Chrome(PATH, options=Chromeoptions)
        driver.get("https://mcdonalds.fast-insight.com/voc/ro/ro")

        time.sleep(5)

        code = driver.find_element_by_id("receiptCode")

        code.send_keys(cod)
        code.send_keys(Keys.RETURN)

        gen = random.choice(['opt_1003736','opt_1003735'])

        varsta = ['opt_1003737','opt_1003738','opt_1003739','opt_1003740','opt_1003741','opt_1003742']

        frecventa = ['opt_1003743','opt_1003744','opt_1003745','opt_1003746','opt_1003747','opt_1003748']

        options = ['opt_1003668','opt_1003673','opt_1003685','opt_1003696','opt_1003704','opt_1003712','opt_1029553','opt_1029558','opt_1029564','opt_1037692']

        frecv = random.choice(frecventa)
        varstaa = random.choice(varsta)

        options.append(gen)
        options.append(frecv)
        options.append(varstaa)

        options.reverse()

        time.sleep(30)

        try:
            button = driver.find_element_by_class_name("btn")
            actions = ActionChains(driver)
            actions.move_to_element(button)
            actions.perform()
            #actions.reset_actions()
            time.sleep(1)

            option = driver.find_element_by_xpath("//*[@data-id='opt_1003724']")
            op = option.find_element_by_css_selector('.opt-data')
            op.click()

            option = driver.find_element_by_name('sbj_1001117[]')
            option.send_keys(random.choice(merite))

            for opt in options:
                try:
                    text = f"//*[@data-id='{opt}']"
                    option = driver.find_element_by_xpath(text)
                    op = option.find_element_by_css_selector('.opt-data')
                    actions.move_to_element(op)
                    actions.perform()
                    op.click()
                except Exception as ex:
                    #print(ex)
                    try:
                        driver.execute_script("scrollBy(0, 250)")
                        op.click()
                        #print(f"Nu merge la: {opt} , pentru ca {ex}")
                    except:
                        pass

            end = driver.find_element_by_class_name('surveycake-logo')
            actions2 = ActionChains(driver)
            actions2.move_to_element(end)
            time.sleep(1000)
            actions2.perform()
            button.click()
            time.sleep(8)

            mail_wrapper = driver.find_element_by_class_name("mail")
            mail = mail_wrapper.find_element_by_name("mail")
            mail.send_keys("cartofissssserie@gmail.com")
            mail.send_keys(Keys.RETURN)
            time.sleep(2)
            #finished = True
            runtimes += 1
            print(f'Feedback completed with code: {cod} | Numer of feedbacks completed: {runtimes}')
            driver.quit()

        except Exception as ex:
            print(ex)
            print(f'Feedback could not be completed with code: {cod}')
            driver.quit()
            return

    except Exception as ex:
        print(f'Feedback could not be completed with code: {cod}')
        print(ex)

if __name__ == "__main__":
    threads = []
    for i in range(0, 50):
        cod = random.choice(codes)
        t = threading.Thread(target=run, args=(cod,))
        threads.append(t)

    i = 0
    while i < len(threads):
        if threading.activeCount() > 12 :
            time.sleep(10)
        else:
            threads[i].start()
            i += 1

    for t in threads:
        t.join()
