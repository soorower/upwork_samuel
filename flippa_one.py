import pandas as pd                                   
from bs4 import BeautifulSoup                          
import requests  
import json
from time import sleep
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Safari/537.36'
}

login_data = {
    'utf8': '✓',
    'session[email]': 'banglabokbok420@gmail.com',
    'session[password]': '5rVQ&FSR',
    'commit': 'Sign in'
    
}

df1 = pd.read_excel('flippa_all_listings.xlsx')
all_links = df1['Listing_url'].tolist()

print(len(all_links))

data_list = []                                         
item = {}
with requests.Session() as s:
    url = 'https://www.flippa.com/sign-in'
    r = s.get(url, headers = headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    login_data['authenticity_token'] = soup.find('input', attrs = {'name':'authenticity_token'})['value']
    
    r = s.post(url, data = login_data, headers = headers)
    link = 'https://flippa.com/search?filter%5Bproperty_type%5D=website,established_website,starter_site&page%5Bsize%5D=6000'
    rs = s.get(link, headers= headers)
    soup = BeautifulSoup(rs.content, 'html5lib')
    links1 = soup.find("div",attrs={'id':'bootstrap-scope'}).find('script',attrs= {'type':'text/javascript'}).get_text().split('const DEFAULT_SEARCH_PARAMS')[0].split('const FILTER_OPTIONS')[1][2:].split('const STATE = ')[1]
    links1 = links1[:-4]

    m = json.loads(links1)
    

    with open('data.json', 'w') as outfile:
        json.dump(m, outfile)
    with open('data.json','r') as file:
        data = json.load(file)
    
    reviews_json = data.get('listings')
    for time,domains,nickname,review_1,review_2,rating1,siteages,profitpmonths,unique_traffics,bid_prices,num_bids,abouts in zip(reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json):
        link3 = time.get('listing_url')
        if link3 in all_links:
            pass
        else:
            print(link3)
            
            property_name = domains.get('property_name')

            title = nickname.get('title')
            country_name = review_1.get('country_name')
            category = review_2.get('category')

            monetization = rating1.get('monetization')
            siteage = siteages.get('formatted_age_in_years')
            profitpmonth = profitpmonths.get('profit_average')
            unique_traffic = unique_traffics.get('uniques_per_month')
            bid_price1 = bid_prices.get('price')
            bid_price = f'${bid_price1} USD'
            num_bid = num_bids.get('bid_count')
            about = abouts.get('summary')
            item = {
                'Listing_url': link3,
                'Domain': property_name,
                'Type': category,
                'Country': country_name,
                'Category': title,
                'Monetization': monetization,
                'Site Age': siteage,
                'Avg net profit per month $': profitpmonth,
                'Avg monthly traffic unique': unique_traffic,
                'Bid price $': bid_price,
                'Number of bids': num_bid,
                'About': about
            }
            data_list.append(item)
            
df = pd.DataFrame(data_list)
done = df.drop_duplicates(keep='first') # removing duplicate rows. index will remain same
dn = done.reset_index(drop=True) #droping previous index
dn.to_excel('flippa_all_listings_today.xlsx') # saving as excel


sleep(3)


import os
import glob
import pandas as pd
import datetime

# os.chdir("D:/Desktop/")
# extension = 'csv'
# all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# print(all_filenames)

all_filenames = []
for file in os.listdir():
    if 'flippa_all_listings.xlsx' in file:
        all_filenames.append(file)
    if 'flippa_all_listings_today.xlsx' in file:
        all_filenames.append(file)
#         print(f'file name: {file}')
print(all_filenames)       
        
        
        
combine = pd.concat([pd.read_excel(f) for f in all_filenames ])
combine.to_excel("flippa_all_listings.xlsx", index=False ,encoding='utf-8')