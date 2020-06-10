import requests
from bs4 import BeautifulSoup as soup
site = 'https://www.melhorcambio.com/dolar-hoje'
header = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
}
site = requests.get(site,headers=header).text
a = soup(site,'html.parser')
b = a.find(class_="text-verde")
dolar_atual = b.attrs['value'].replace(',','.')
print(f'O dólar atualmente está em R$ {dolar_atual}')





