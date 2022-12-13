#Código com while e for

from bs4 import BeautifulSoup
from requests_html import HTMLSession
import lxml
import pandas as pd

session = HTMLSession()
url = session.get("https://lista.mercadolivre.com.br/celular#component_id=MOST_WANTED")
soup = BeautifulSoup(url.text, "lxml")


data = {'Titulo': [], 'Preço': [], 'Imagem': [], 'Produto': []}
tb = pd.DataFrame(data=data)
c = 0

items = soup.find_all("li", {"class": "ui-search-layout__item shops__layout-item"})
total = int(soup.find("li", {"class": "andes-pagination__page-count"}).text.split('de ')[1])
next = str(soup.find("a", {"class": "andes-pagination__link shops__pagination-link ui-search-link"})).split('href="')[1].split('"')[0]
for i in items:
    title = i.find("h2", {"class": "ui-search-item__title shops__item-title"}).text
    price = i.find("span", {"class": "price-tag-fraction"}).text
    imglink = str(i.find("img")).split('src="')[1].split('"')[0]
    productlink = str(i.find("a", {"class": "ui-search-link"})).split('href="')[1].split('"')[0]
    tb.loc[c, 'Titulo'] = title
    tb.loc[c, 'Preço'] = price
    tb.loc[c, 'Imagem'] = imglink
    tb.loc[c, 'Produto'] = productlink
    c += 1
#display(tb)
while True:
    try:
        url = session.get(next)
        soup = BeautifulSoup(url.text, "lxml")

        items = soup.find_all("li", {"class": "ui-search-layout__item shops__layout-item"})
        for i in items:
            title = i.find("h2", {"class": "ui-search-item__title shops__item-title"}).text
            price = i.find("span", {"class": "price-tag-fraction"}).text
            imglink = str(i.find("img")).split('src="')[1].split('"')[0]
            productlink = str(i.find("a", {"class": "ui-search-link"})).split('href="')[1].split('"')[0]
            tb.loc[c, 'Titulo'] = title
            tb.loc[c, 'Preço'] = price
            tb.loc[c, 'Imagem'] = imglink
            tb.loc[c, 'Produto'] = productlink
            c += 1
        next = str(soup.find_all("a", {"class": "andes-pagination__link shops__pagination-link ui-search-link"})[1]).split('href="')[1].split('"')[0]
        break # Quebra na primeira pra não executar todas
    except:
        break        
        
        
for ii in range(1, total + 1):
    ii = ii * 50 + 1
    url = session.get(f"https://lista.mercadolivre.com.br/celulares-telefones/celulares-smartphones/celular_Desde_{ii}_NoIndex_True")
    soup = BeautifulSoup(url.text, "lxml")
    
    items = soup.find_all("li", {"class": "ui-search-layout__item shops__layout-item"})
    for i in items:
        title = i.find("h2", {"class": "ui-search-item__title shops__item-title"}).text
        price = i.find("span", {"class": "price-tag-fraction"}).text
        imglink = str(i.find("img")).split('src="')[1].split('"')[0]
        productlink = str(i.find("a", {"class": "ui-search-link"})).split('href="')[1].split('"')[0]
        tb.loc[c, 'Titulo'] = title
        tb.loc[c, 'Preço'] = price
        tb.loc[c, 'Imagem'] = imglink
        tb.loc[c, 'Produto'] = productlink
        c += 1
    break # Quebra na primeira pra não executar todas
        
display(tb)
tb.to_excel('products.xlsx', index=None)


#Código 1

from bs4 import BeautifulSoup
from requests_html import HTMLSession
import lxml
import pandas as pd

session = HTMLSession()
url = session.get("https://lista.mercadolivre.com.br/celular#component_id=MOST_WANTED")
soup = BeautifulSoup(url.text, "lxml")


data = {'Titulo': [], 'Preço': [], 'Imagem': [], 'Produto': []}
tb = pd.DataFrame(data=data)
c = 0

items = soup.find_all("li", {"class": "ui-search-layout__item shops__layout-item"})
total = int(soup.find("li", {"class": "andes-pagination__page-count"}).text.split('de ')[1])
for i in items:
    title = i.find("h2", {"class": "ui-search-item__title shops__item-title"}).text
    price = i.find("span", {"class": "price-tag-fraction"}).text
    imglink = str(i.find("img")).split('src="')[1].split('"')[0]
    productlink = str(i.find("a", {"class": "ui-search-link"})).split('href="')[1].split('"')[0]
    tb.loc[c, 'Titulo'] = title
    tb.loc[c, 'Preço'] = price
    tb.loc[c, 'Imagem'] = imglink
    tb.loc[c, 'Produto'] = productlink
    c += 1
        
for ii in range(1, total + 1):
    ii = ii * 50 + 1
    url = session.get(f"https://lista.mercadolivre.com.br/celulares-telefones/celulares-smartphones/celular_Desde_{ii}_NoIndex_True")
    soup = BeautifulSoup(url.text, "lxml")
    
    items = soup.find_all("li", {"class": "ui-search-layout__item shops__layout-item"})
    for i in items:
        title = i.find("h2", {"class": "ui-search-item__title shops__item-title"}).text
        price = i.find("span", {"class": "price-tag-fraction"}).text
        imglink = str(i.find("img")).split('src="')[1].split('"')[0]
        productlink = str(i.find("a", {"class": "ui-search-link"})).split('href="')[1].split('"')[0]
        tb.loc[c, 'Titulo'] = title
        tb.loc[c, 'Preço'] = price
        tb.loc[c, 'Imagem'] = imglink
        tb.loc[c, 'Produto'] = productlink
        c += 1
        
display(tb)
tb.to_excel('products.xlsx', index=None)

