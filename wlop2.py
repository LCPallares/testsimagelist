import requests, bs4, json


url = "https://wlop.artstation.com/"
peticion = requests.get(url)
sopa = bs4.BeautifulSoup(peticion.text, "lxml")

Datos = []
for principal in sopa.find_all(class_="album-grid-item"):
    Diccionario = {
        "post": url + principal.find('a')['href'],
        "miniaturas": principal.find(class_="img-fluid")['src'],
        "titulo": principal.find(class_="album-grid-item-name").text,
    }
    Datos.append(Diccionario)

with open('wlop.json', 'w') as outfile:
    json.dump(Datos, outfile)
