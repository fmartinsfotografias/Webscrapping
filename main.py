from bs4 import BeautifulSoup
import requests
import smtplib
import email.message
from time import sleep
from urllib.request import urlopen,urlretrieve
import pandas as pd

#BemVindo
print('='*60)
print('SEJA BEM VINDO(a)'.center(60))
print('='*60)

sleep(2)

#Cadastro da URL rastreamento
URL = str(input('Qual Link deseja rastrear: '))
valor = float(input('Qual valor quer pagar R$: '))
# Cadastro do Usuario
nome = input(str('Qual seu nome: ')).strip().capitalize()
#Validação do email cadastrado
while True:
     cadastro_email = str(input('Qual seu e-mail: '))
     if not "@" in cadastro_email:
       print('Email invalido!!!')
     else:
        break


#Coleta das informações na página
headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72"}
site = requests.get(URL, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find('h1', class_ = 'header-product__title').get_text()
price = soup.find('div', class_ = 'price-template-price-block').get_text().strip()

#imprimindo as informações na tela
print('='*60)
print(f'Ok Sr(a) {nome}, {title} cadastrado com sucesso,  estamos rastreando ')
print(f'Você esta disposto a pagar abaixo de R$ {valor:.2f}')
print(f'Agora o {title} \nesta custando R$ {price}')

#fatiamentos para tratamento
num_price = price[7:15]
num_price = num_price.replace('.','')
num_price = num_price.replace(',','')
num_price = float(num_price)


# função enviar email
def send_email():
    email_content = f"""{URL}"""
    msg = email.message.Message()
    msg['subject'] = f'Preço do {title} baixou!!!'
    msg['From'] = 'contato@fotografandosentimentos.com'
    msg['To'] = cadastro_email
    password = '@Fernando270820'
    msg.add_header('Content-type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'],password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())

    print('Sucesso ao enviar o Email')
print('='*60)

#função para verificação de valor
if valor < num_price:
    send_email()
else:
     print(f'{nome}, sem alterações no momento para o {title}, \nvalor atual {price}')