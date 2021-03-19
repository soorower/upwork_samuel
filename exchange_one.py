import pandas as pd                                   
from bs4 import BeautifulSoup                          
import requests  
import datetime
from time import sleep

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Safari/537.36'
}

data = []
list = {}
counter = 0
for i in range(1,417):
    sleep(5)
    counter += 1
    print(counter)
    url = f'https://exchangemarketplace.com/shops?page={i}&sortBy=businessHealthTierHighToLow'
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.content, 'html5lib')
#     print(r.content)

    listing_link = []
    
    for link in soup.findAll('a', attrs={'class': '_3gf3d xQBnN _1oHwA'}):
        links = link.get('href')
        links1 = f'https://exchangemarketplace.com{links}'
        listing_link.append(links1)
        list = {
            'links': links1
        }
        data.append(list)

    print(len(listing_link))

df = pd.DataFrame(data)
done = df.drop_duplicates(keep='first') # removing duplicate rows. index will remain same
dn = done.reset_index(drop=True) #droping previous index
dn.to_excel('exchange_all_listings.xlsx',index= False) # saving as excel