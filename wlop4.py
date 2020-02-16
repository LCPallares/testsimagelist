#coding: utf-8
import requests
from bs4 import BeautifulSoup
from time import sleep
import json
import csv
import pandas as pd


URL_BASE = 'https://wlop.artstation.com/'


def make_soup(url):
    peticion = requests.get(url)
    return BeautifulSoup(peticion.text, "lxml")


Datos = []


def obtener_enlaces(sopa):
    for x in sopa.find_all(class_="album-grid-item"):
        Diccionario = {
            "post": URL_BASE + x.find('a')['href'],
            "miniaturas": x.find(class_="img-fluid")['src'],
            "titulo": x.find(class_="album-grid-item-name").text,
        }
        Datos.append(Diccionario)


if __name__ == '__main__':
    sopa = make_soup(URL_BASE)
    enlaces = obtener_enlaces(sopa)
    # print(enlaces)

    with open('wlop.json', 'w') as outfile:
        json.dump(Datos, outfile)
