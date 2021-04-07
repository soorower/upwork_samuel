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

df1 = pd.read_excel('exchange_all_listings.xlsx')
all_links = df1['links'].tolist()
print(len(all_links))
data = []
list = {}
counter = 0
for i in range(1,417):
#     sleep(2)
    counter += 1
    print(counter)
    url = f'https://exchangemarketplace.com/shops?page={i}&sortBy=businessHealthTierHighToLow'
    try:
        r = requests.get(url, headers = headers,timeout=8)
    except:
        print('request timeout')
    sleep(3)
    soup = BeautifulSoup(r.content, 'html5lib')
#     print(r.content)

    listing_link = []
    
    for link in soup.findAll('a', attrs={'class': '_3gf3d xQBnN _1oHwA'}):
        links = link.get('href')
        links1 = f'https://exchangemarketplace.com{links}'
        listing_link.append(links1)
        if links1 in all_links:
            pass
        else:
            print(links1)
            list = {
            'links': links1
            }
            
            
        try:
            data.append(list)
        except:
            pass


    print('Total links found in one page:',len(listing_link))

df = pd.DataFrame(data)
done = df.drop_duplicates(keep='first') # removing duplicate rows. index will remain same
dn = done.reset_index(drop=True) #droping previous index
dn.to_excel('exchange_all_listings_today.xlsx',index= False) # saving as excel

sleep(3)


import os
import glob
import pandas as pd
import datetime
x = datetime.datetime.now()
hour = x.hour
minute = x.minute
date_1= x.day
month = x.month
year = x.year
date_time1 = f'{date_1}-{month}-{year}_{hour}-{minute}'



# os.chdir("D:/Desktop/")
# extension = 'csv'
# all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# print(all_filenames)

all_filenames = []
for file in os.listdir():
    if 'exchange_all_listings.xlsx' in file:
        all_filenames.append(file)
    if 'exchange_all_listings_today.xlsx' in file:
        all_filenames.append(file)
#         print(f'file name: {file}')
print(all_filenames)       
        
        
        
combined_csv = pd.concat([pd.read_excel(f) for f in all_filenames ])
combined_csv.to_excel("exchange_all_listings.xlsx", index=False ,encoding='utf-8')