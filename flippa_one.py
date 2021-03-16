import pandas as pd                                   
from bs4 import BeautifulSoup                          
import requests  
import json

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


with requests.Session() as s:
    url = 'https://www.flippa.com/sign-in'
    r = s.get(url, headers = headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    login_data['authenticity_token'] = soup.find('input', attrs = {'name':'authenticity_token'})['value']
    
    r = s.post(url, data = login_data, headers = headers)
    link = 'https://flippa.com/search?filter%5Bproperty_type%5D=website,established_website,starter_site&page%5Bsize%5D=5388'
    rs = s.get(link, headers= headers)
    soup = BeautifulSoup(rs.content, 'html5lib')
    links1 = soup.find("div",attrs={'id':'bootstrap-scope'}).find('script',attrs= {'type':'text/javascript'}).get_text().split('const DEFAULT_SEARCH_PARAMS')[0].split('const FILTER_OPTIONS')[1][2:].split('const STATE = ')[1]
    links1 = links1[:-4]

    m = json.loads(links1)
    data_list = []                                         
    item = {}

    with open('data.json', 'w') as outfile:
        json.dump(m, outfile)
    with open('data.json','r') as file:
        data = json.load(file)
    
    reviews_json = data.get('listings')
    for time,domains,nickname,review_1,review_2,rating1,siteages,profitpmonths,unique_traffics,bid_prices,num_bids,abouts in zip(reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json,reviews_json):
        date = time.get('listing_url')
        domain = domains.get('property_name')

        reviewer = nickname.get('title')

        review_title = review_1.get('country_name')

        review_text = review_2.get('category')

        rating = rating1.get('monetization')
        siteage = siteages.get('formatted_age_in_years')
        profitpmonth = profitpmonths.get('profit_average')
        unique_traffic = unique_traffics.get('uniques_per_month')
        bid_price = bid_prices.get('price')
        num_bid = num_bids.get('bid_count')
        about = abouts.get('summary')
        item = {
            'Listing_url': date,
            'Domain': domain,
            'Type': review_text,
            'Country': review_title,
            'Category': reviewer,
            'Monetization': rating,
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
    dn.to_csv('flippa.csv') # saving as csv