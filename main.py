import requests
import xmltodict

url = 'https://www.w3schools.com/xml/cd_catalog.xml'

resposta = requests.get(url)
dicionario = xmltodict.parse(resposta.content)
catalogo = dicionario['CATALOG']['CD']

for titulo_cd in catalogo:
    print(titulo_cd['TITLE'])
