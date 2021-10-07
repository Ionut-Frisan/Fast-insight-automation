from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions
import time
import random
import generate_code
import threading
import multiprocessing
from datetime import date
import os,sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

SCROLL_PAUSE_TIME = 0.5

Chromeoptions = ChromeOptions()
#Chromeoptions.add_argument("--incognito")

PATH = "chromedriver.exe"

codes = generate_code.get_codes('0dfwd9yumu3l', 500)
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

def addNewMerit(merit):
    merite.append(merit)

today = date.today().strftime("%d/%m/%Y")
Separator = "   ----------------------"+ today + "----------------------   " + '\n'
with open("log.txt", "a+") as f:
    f.write(Separator)
    f.close()


def run(cod, queue):
    global runtimes
    global finished
    global Chromeoptions
    global merite
    global PATH
    with open("log.txt", 'a+') as f:
        try:
            Chromeoptions.add_argument("--log-level=OFF")
            Chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
            Chromeoptions.add_argument("window-size=1280,800")
            Chromeoptions.add_experimental_option("excludeSwitches", ['enable-automation'])

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
                        try:
                            driver.execute_script("scrollBy(0, 250)")
                            op.click()
                        except:
                            pass

                end = driver.find_element_by_class_name('surveycake-logo')
                actions2 = ActionChains(driver)
                actions2.move_to_element(end)
                for j in range(150):
                    if("survey.fast-insight.com/mcd/ro/voucher.php" in driver.current_url):
                        runtimes+=1
                        f.write(f'Feedback completed with code: {cod} | Numer of feedbacks completed: {runtimes} \n')
                        f.close()
                        queue.put(1)
                        print(f'Feedback completed with code: {cod} | Numer of feedbacks completed: {runtimes} \n')
                        time.sleep(3)
                        mail_wrapper = driver.find_element_by_class_name("mail")
                        mail = mail_wrapper.find_element_by_name("mail")
                        mail.send_keys("cartofissssserie@gmail.com")
                        mail.send_keys(Keys.RETURN)
                        time.sleep(2)
                        driver.quit()
                        break
                    else:
                        time.sleep(1)
                #time.sleep(100)
                #actions2.perform()
                #button.click()
                #time.sleep(8)
                driver.quit()

            except Exception as ex:
                print(ex)
                f.write(f'Feedback could not be completed with code: {cod} \ {ex} \n')
                f.close()
                print(f'Feedback could not be completed with code: {cod} \n')
                driver.quit()
                return

        except Exception as ex:
            f.write(f'Feedback could not be completed with code: {cod} | {ex}\n')
            f.close()
            print(f'Feedback could not be completed with code: {cod}')
            print(ex)
            return

if __name__ == "__main__":
    threads = []
    for i in range(0, 50):
        cod = random.choice(codes)
        t = threading.Thread(target=run, args=(cod,))
        threads.append(t)

    i = 0
    while i < len(threads):
        if threading.activeCount() > multiprocessing.cpu_count() :
            time.sleep(10)
        else:
            threads[i].start()
            i += 1

    for t in threads:
        t.join()
