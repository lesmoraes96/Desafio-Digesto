# Desafio Phyton Disgesto

import requests
import pandas as pd
from bs4 import BeautifulSoup

#Escolha da etapa para a aplicação
etapa = input("Defina a etapa da aplicação:")
if etapa not in '1 2 3 4':
    print("Etapa invalida, tente novamente!")
    exit()

#Função WebScrapping site Vultr
def raw_data(source):
    aux = 0
    y = 0
    soup = BeautifulSoup(source, 'lxml')
    data = []
    rdata = soup.find_all('strong')
    for x in range(len(rdata)):
        if 'Faster' not in rdata[x].text:
            data.append(rdata[x].text)
    data = data[:50]
    L1 = []
    L2 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    L7 = []
    L8 = []
    L9 = []
    L10 = []
    rows = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10]
    for y in range(10):
        for x in range(5):
            rows[y].append(data[aux])
            aux += 1
    df = pd.DataFrame(rows, index = ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]', '[10]'], columns = ['STORAGE','CPU', 'MEMORY', 'BANDWITH','PRICE[%/mo]',])
    if etapa == '3' or etapa == '4':
        df.to_csv('Vultr.csv')
    if etapa == '2'or etapa == '3' or etapa == '4':
        df.to_json('Vultr.json')
    return(df)
    

#Site Vultr
url = 'https://www.vultr.com/products/cloud-compute/'
r = requests.get(url)
print("\nVultr\n")
print(raw_data(r.text))
    
#Site Digital Ocean    
if etapa == '4':
    url2 = 'https://www.digitalocean.com/pricing/#droplet'
    r2 = requests.get(url2)
    df2 = pd.read_html(r2.text)[0]
    df2.to_csv('DigitalOcean.csv')
    df2.to_json('DigitalOcean.json')
    print("\nDigital Ocean\n")
    print(df2[['Memory', 'vCPUs', 'Transfer', 'SSD Disk', 'Price']])


