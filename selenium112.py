from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions
import time
import random
import generate_code
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import captcha_solver


SCROLL_PAUSE_TIME = 0.5

Chromeoptions = ChromeOptions()
#Chromeoptions.add_argument("--incognito")

PATH = "D:\Python projects\chromedriver.exe"

codes = generate_code.get_codes('odfw0hyeznn9', 500)
#print(codes)

runtimes = 0
finished = False

proxies = ['193.56.255.131','31.14.49.1','193.239.86.248','89.47.120.66','193.56.255.179','193.56.255.181','193.239.86.137','193.239.86.249','193.56.255.180','86.123.166.109','89.238.255.34']

def run(cod):
    global runtimes
    global finished
    global Chromeoptions
    global proxies
    try:
        ua = UserAgent()
        #userAgent = ua.random
        userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324 Safari/14.0.3'
        print(userAgent)
        Chromeoptions.add_argument("start-maximized")
        Chromeoptions.add_experimental_option("excludeSwitches", ["enable-automation"])
        Chromeoptions.add_experimental_option('useAutomationExtension', False)
        Chromeoptions.add_argument(f'user-agent={userAgent}')
        Chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
        #Chromeoptions.add_argument("window-size=1920,1080")
        proxy = random.choice(proxies)
        #Chromeoptions.add_argument('proxy-server=193.56.255.131')

        driver = webdriver.Chrome(PATH, options=Chromeoptions)
        #driver = webdriver.Chrome(PATH)

        #driver.maximize_window()

        driver.get("https://mcdonalds.fast-insight.com/voc/ro/ro")

        time.sleep(2)

        code = driver.find_element_by_id("receiptCode")

        code.send_keys(cod)
        code.send_keys(Keys.RETURN)

        #opt1 = driver.find_element_by_class_name("opt-data").click()

        merite = ['Totul a fost ok','Minunat','de vis','excelent','a fost ok','angajati seriosi, manageri pertinenti','per total a fost super','mancarea a fost foarte buna si proaspata','inghetata e excelenta','am fost serviti foarte repede si comanda a fost intreaga','mediul este unul foarte placut','mancarea e geniala!!!','puisor is life','kutgw','as recomanda cu dra','mirobolant','Mi-a lasat o impresie foarte buna aceasta experienta','tineti-o tot asa!','10/10','super super <3','ofertele de pe aplicatie','Toti angajatii','echipa foarte frumoasa','mancare proaspata','atmosfera placuta','amabilitate','zambetele se vad si prin masti :)','servirea rapida','rapiditate si mancare buna','asd','.','tot','totul','curatenia','mediul este placut si angajatii isi fac treaba foarte bine','am avut o problema pe aplicatie,dar m-a ajutat un manager.foarte seriosi si pregatiti']

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

        time.sleep(15)

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
            actions2.perform()

            try:
                #WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
                #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
                #time.sleep(2)
                captcha = captcha_solver.SyncMe()
                captcha.do_captcha(driver)
            except Exception as ex:
                print(ex)
            time.sleep(60)
            button.click()
            time.sleep(8)

            mail_wrapper = driver.find_element_by_class_name("mail")
            mail = mail_wrapper.find_element_by_name("mail")
            mail.send_keys("cartofissssserie@gmail.com")
            mail.send_keys(Keys.RETURN)
            time.sleep(2)
            finished = True
            runtimes += 1
            driver.quit()
        except Exception as ex:
            print(ex)
            #am adaugat driver.quit() - 30.12.2020 - daca exista buguri de aici e baiu
            driver.quit()
            return

    except Exception as ex:
        print(ex)
        #run()

for i in range(0,len(codes)):
    cod = random.choice(codes)
    finished = False
    run(cod)
    if finished == True :
        print(f'Feedback completed with code: {cod} | Numer of feedbacks completed: {runtimes}')
    else:
        print(f'Feedback could not be completed with code: {cod}')

#for cod in codes:
    #run(cod)

