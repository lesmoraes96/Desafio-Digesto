import requests
import pandas as pd
from bs4 import BeautifulSoup


urlVultr = 'https://www.vultr.com/products/cloud-compute/'
urlOcean = 'https://www.digitalocean.com/pricing/#droplet'



#raw data DigitalOcean
def digitalocean(source1):

    r = requests.get(source1).text

    df1 = pd.read_html(r)[0]

    return (df1[['Memory', 'vCPUs', 'Transfer', 'SSD Disk', 'Price']])
#raw data DigitalOcean

#raw data Vultr
def vultr(source):
    r = requests.get(source).text
    aux = 0
    y = 0
    soup = BeautifulSoup(r, 'lxml')
    data = []
    rdata = soup.find_all('strong')
    for x in range(len(rdata)):
        if 'Faster' not in rdata[x].text:
            data.append(rdata[x].text)
    data = data[:50]
#rows
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
#rows
    df = pd.DataFrame(rows, index = ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]', '[10]'], columns = ['STORAGE','CPU', 'MEMORY', 'BANDWITH','PRICE[%/mo]',])
    return(df)
#raw data
n = True
print('-- Digesto Web Scraping --')
while n:
    k = True
    menu = input('\t[MENU]\n[1] https://www.vultr.com/pricing/\n[2] https://www.digitalocean.com/pricing/#droplet\n[0] exit\n')
    if menu == '0':
        n = not n
    elif menu == '1':
        while k:
            menu = input('[1]--print\n[2]--save_csv\n[3]--save_json\n[0]--return\n')
            if menu == '0':
                k = not k
            elif menu == '1':
                print(vultr(urlVultr))
            elif menu == '2':
                export_csv =  vultr(urlVultr).to_csv ('vultr.csv', index = None, header=True)
                print('Operação realizada com sucesso.')
            elif menu == '3':
                export_csv = vultr(urlVultr).to_json ('vultr.json')
                print('Operação realizada com sucesso.')
            else:
                print('Opção inválida, tente novamente.')
    elif menu == '2':
        while k:
            menu = input('[1]--print\n[2]--save_csv\n[3]--save_json\n[0]--return\n')
            if menu == '0':
                k = not k
            elif menu == '1':
                print(digitalocean(urlOcean))
            elif menu == '2':
                export_csv = digitalocean(urlOcean).to_csv ('DigitalOcean.csv', index = None, header=True)
                print('Operação realizada com sucesso.')
            elif menu == '3':
                export_csv = digitalocean(urlOcean).to_json ('DigitalOcean.json')
                print('Operação realizada com sucesso.')
            else:
                print('Opção inválida, tente novamente.')
    else:
        print('Opção inválida, tente novamente.')