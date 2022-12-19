import pytesseract as ts
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

async def agendar(context, data):
    def delay ():
        time.sleep(0.5)
    options = Options()
    options.add_argument("--headless");

    driver = webdriver.Firefox(options=options)

    baseLink = "https://portal.ufsm.br/ru/usuario/agendamento/form.html"

    driver.get(baseLink)
    login = data[0];
    driver.find_element(By.ID, 'login').send_keys(login)
    password = data[1];
    driver.find_element(By.ID, 'senha').send_keys(password)
    driver.find_element(By.NAME, 'enter').click()

    ok = False

    while (not(ok)):
        try:
            startDate = datetime.now() + timedelta(1)
            driver.find_element(By.ID, 'data').send_keys(startDate.strftime('%d/%m/%Y'))

            endDate = datetime.now() + timedelta(3)
            driver.find_element(By.ID, 'periodo_fim').send_keys(endDate.strftime('%d/%m/%Y'))

            res = Select(driver.find_element(By.ID, 'restaurante'))
            res.select_by_visible_text("RU - Campus I")
            delay()

            driver.find_element(By.ID, 'checkTipoRefeicao1').click()
            driver.find_element(By.ID, 'checkTipoRefeicao3').click()

            driver.find_element(By.ID, 'opcaoVegetariana_false').click()
            img = driver.find_element(By.ID, 'imgCaptcha').screenshot("Captcha.png")
            delay()

            text = ts.image_to_string("Captcha.png")
            print(text);
            driver.find_element(By.ID, 'captcha').clear()
            driver.find_element(By.ID, 'captcha').send_keys(text.replace(" ", ""))

            driver.find_element(By.ID, 'btnSubmit').click()

            delay()

            try:
                if driver.find_element(By.ID, '_captcha').is_displayed():
                    delay()
                    await context.channel.send('Deu pau no captcha gurizada, tentando de novo...');
                    ok = False
                else:
                    ok = True
            except:
                ok = True
        except:
            await context.channel.send('Deu pau gurizada, tentando de novo...');
            ok = False
            delay()

    delay()

    ok = False

    while (not(ok)):
        try:
            startDate = datetime.now() + timedelta(1)
            driver.find_element(By.ID, 'data').send_keys(startDate.strftime('%d/%m/%Y'))
            endDate = datetime.now() + timedelta(3)
            driver.find_element(By.ID, 'periodo_fim').send_keys(endDate.strftime('%d/%m/%Y'))

            res = Select(driver.find_element(By.ID, 'restaurante'))
            res.select_by_visible_text("RU - Campus II")

            delay()

            driver.find_element(By.ID, 'checkTipoRefeicao2').click()

            driver.find_element(By.ID, 'opcaoVegetariana_false').click()

            img = driver.find_element(By.ID, 'imgCaptcha').screenshot("Captcha.png")

            delay()

            text = ts.image_to_string("Captcha.png")
            driver.find_element(By.ID, 'captcha').clear()
            driver.find_element(By.ID, 'captcha').send_keys(text.replace(" ", ""))

            driver.find_element(By.ID, 'btnSubmit').click()

            delay()

            try:
                if driver.find_element(By.ID, '_captcha').is_displayed():
                    delay()
                    await context.channel.send('Deu pau no captcha gurizada, tentando de novo...');
                    ok = False
                else:
                    ok = True
            except:
                ok = True
            
        except:
            await context.channel.send('Deu pau gurizada, tentando de novo...');
            ok = False
            delay()

    await context.reply('Feito');
    driver.quit()