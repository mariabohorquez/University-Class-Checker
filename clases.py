# Para que este programa corra se necesita instalar python 3.6
# Mas los modulos: BeautifulSoup que no vienen con python

import requests
from bs4 import BeautifulSoup
import re

# how to keep cookies turned on to scrape next page:
# https://stackoverflow.com/questions/8316818/login-to-website-using-python/8316989

# page where I got the idea from:
# https://www.twilio.com/blog/2017/06/hacked-my-universitys-registration-system-python-twilio.html

def asking():
    USER = input("Introduzca el usuario: \n> ")
    PASSWORD = input("Introduzca la contraseña: \n> ")
    return USER, PASSWORD

def get_page(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup = soup.get_text()
    print(soup)
    # r = re.compile(r"(http://[^ ]+)")
    # print(r.sub(r'<a href="\1">\1</a>', soup)

def login():
    pass

def find_word():
    soup = soup.get_text()
    print(soup)


def main():
    while True:
        print("Bienvenido a PageOpen.")
        print("Le avisaremos cuando una palabra específica aparezca en la página.")
        print("¿Qué página es? Por favor copie y pegue el url completo.")
        URL = input("> ")
        print(f"Confirme que su página es {URL}.")
        print("[y/n]")
        if input("> ") == 'y':
            break
        else:
            continue

    get_page(URL)

main()
