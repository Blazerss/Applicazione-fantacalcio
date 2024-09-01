from bs4 import BeautifulSoup as bs
import requests
import csv
import pandas as pd

ruoli = ['Portieri',
       'Difensori',
        'Centrocampisti', 'Trequartisti', 'Attaccanti'
         ]

# Carica il file Excel con i dati dei calciatori
df = pd.read_excel("C:/Users/bront/OneDrive/Desktop/Quotazioni_Fantacalcio_Stagione_2024_25.xlsx", header=1)
listName = df['Nome']
df.set_index("Nome", inplace=True)
calciatori = []
for ruolo in ruoli:
   html = requests.get("https://www.fantacalciopedia.com/lista-calciatori-serie-a/" + ruolo.lower() + "/")
   soup =  bs(html.content,"html.parser")
   g = soup.find_all("div", class_= "col_full giocatore")
   for t in g:
       calciatori.append(t.find("a").get("href"))

with open('asta1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    field = ["Nome","ALG FTP", "FM 23-24", "FM 22-23", "FM 21-22 ", "attributi","Res. Inf."]
    writer.writerow(field)
    for y in calciatori:
        print(y)
        html2 = requests.get(y)
        #estrai attributi
        soup2 = bs(html2.content, "html.parser")
        nome = soup2.find_all("div",class_="fancy-title title-bottom-border")[0].h1.get_text().strip().lower().capitalize()
        tokens = nome.split()
        parole_da_verificare = ['di', 'de', "del"]
        if len(tokens) > 1 and tokens[0].lower() in parole_da_verificare:
             nome = tokens[0].capitalize() + ' ' + tokens[1].capitalize()
        else:
            nome = tokens[0]
        g = soup2.find("div", class_="col_full center mc_hookEvolution")
        g = g.find_all("div", class_="col_one_fourth")
        attrs = []
        for j in g:
            attrs.append(j.find("span", class_="stickdanpic").get_text().strip())


        #estrai medie fantavoto
        g = soup2.find("div", class_="col_three_fourth")
        g = g.find_all("div", class_="col_one_fourth")
        FM = []
        for j in g:
            FM.append(j.find("span", class_="stickdan").get_text().strip())
        g=soup2.find_all("div", class_="counter counter-inherit counter-instant")
        inf = g[-1].text



        writer.writerow([nome,FM[0],FM[1],FM[2],FM[3],attrs,inf])



