import requests
import smtplib
import email.message
from lxml import html
from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep

# PROXY = '91.224.62.194:8080'
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'--proxy-server={PROXY}')


URL = "https://sisgcorp.eb.mil.br"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
sleep(5)
driver.find_element_by_xpath('//*[@id="redirecionarPBC"]').click()
sleep(1.5)
driver.find_element_by_name("accountId").send_keys("34762774880")
sleep(2)
driver.find_element_by_xpath('//*[@id="login-button-panel"]/button').click()
sleep(1)
driver.find_element_by_name("password").send_keys("@Fernando07101986#")
sleep(2)
driver.find_element_by_xpath('//*[@id="submit-button"]').click()
sleep(15)
driver.find_element_by_xpath('/html/body/app-root/sisgcorp-secured-layout/div/div/div[1]/div/div[1]/app-menu/ul/li/a/span[1]/div').click()
sleep(2)
driver.find_element_by_xpath('/html/body/app-root/sisgcorp-secured-layout/div/div/div[1]/div/div[1]/app-menu/ul/li/ul/li/a/span[1]/div').click()
sleep(2)
driver.find_element_by_xpath('/html/body/app-root/sisgcorp-secured-layout/div/div/div[1]/div/div[1]/app-menu/ul/li/ul/li/ul/li[3]/a/span/div').click()
sleep(2)
dados = driver.find_element_by_xpath('/html/body/app-root/sisgcorp-secured-layout/div/div/div[2]/div/sisgcorp-listar-processos/div/div/div/div/ebc-datatable/div/div[1]')
html_content = dados.get_attribute('outerHTML')

print(html_content)



# headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72"}
# soup = BeautifulSoup(site.content, 'html.parser')
#
#
# headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72"}


driver.quit()
# def send_email():
#     email_content = """
#     https://www.magazineluiza.com.br/smartphone-samsung-galaxy-s22-ultra-256gb-preto-5g-12gb-ram-68-cam-quadrupla-selfie-40mp/p/234440600/te/s22u/
# """
#     msg = email.message.Message()
#     msg['subject'] = 'Preço do Celular S22 ultra baixou!!! COOORRRREEEEE!!!!'
#     msg['From'] = 'contato@fotografandosentimentos.com'
#     msg['To'] = 'contato@fotografandosentimentos.com'
#     password = '@Fernando270820'
#     msg.add_header('Content-type', 'text/html')
#     msg.set_payload(email_content)
#
#     s = smtplib.SMTP('smtp.gmail.com: 587')
#     s.starttls()
#     s.login(msg['From'],password)
#     s.sendmail(msg['From'], [msg['To']], msg.as_string())
#
#     print('Sucesso ao enviar o Email')
#
#
# if num_price > 9400:
#     send_email()