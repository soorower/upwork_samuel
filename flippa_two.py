import pandas as pd                                   
from bs4 import BeautifulSoup                          
import requests  
import datetime
from itertools import cycle
import traceback

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

df = pd.read_excel('flippa_all_listings_today.xlsx')

x = datetime.datetime.now()
hour = x.hour
minute = x.minute
date_1= x.day
month = x.month
year = x.year
date_time1 = f'{date_1}-{month}-{year}_{hour}-{minute}'
date_time = f'{date_1}-{month}-{year} {hour}:{minute}'
    
all_links_collected_to_csv = df['Listing_url'].tolist()
domain = df['Domain'].tolist()
types = df['Type'].tolist()
country_a = df['Country'].tolist()
category = df['Category'].tolist()
monetization = df['Monetization'].tolist()
site_age = df['Site Age'].tolist()
avg_net_profit_per_month = df['Avg net profit per month $'].tolist()
avg_monthly_traffic_unique = df['Avg monthly traffic unique'].tolist()
bid_price = df['Bid price $'].tolist()
number_of_bids = df['Number of bids'].tolist()
# about = df['About'].tolist()
data = []
lists = {}


with requests.Session() as s:
    url = 'https://www.flippa.com/sign-in'
    r = s.get(url, headers = headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    login_data['authenticity_token'] = soup.find('input', attrs = {'name':'authenticity_token'})['value']
    
    r = s.post(url, data = login_data, headers = headers)
    counts = 0
    name = 'Flippa'
    for link,a1,b1,c1,d1,e1,f1,g1,h1,i1,j1 in zip(all_links_collected_to_csv,domain,types,country_a,category,monetization,site_age,avg_net_profit_per_month,avg_monthly_traffic_unique,bid_price,number_of_bids):
        counts += 1
        ids = link.split('/')[3]
        print(counts)
        print(link)
        rs = s.get(link, headers= headers)
        soup = BeautifulSoup(rs.content, 'html.parser')
#         print(rs.content)
        
#----------------------------------------------------------------------------------------------
        try:
            platform = soup.find('div',attrs= {'id':'platform'}).get_text().strip()    
        except:
            platform = '-'
        
#----------------------------------------------------------------------------------------------
        try:
            avg_rev_per_month = soup.find('div',attrs= {'id':'gross_revenue'}).get_text().strip()[1:-4]
        except:
            avg_rev_per_month = '-'

#----------------------------------------------------------------------------------------------
        try:
            prof_box = soup.find('div',attrs={'class':'Chart Chart--snapshot Chart--snapshotMd'})
        except:
            pass
#----------------------------------------------------------------------------------------------
        try:
            traffic_box = soup.find('div',attrs= {'class':'Chart Chart--snapshot'})
        except:
            pass
#----------------------------------------------------------------------------------------------
        try:
            profit = prof_box['profit-data'].split(',')
        except:
            pass
#----------------------------------------------------------------------------------------------
        try:
            revenue = prof_box['gross-data'].split(',')
        except:
            pass
#----------------------------------------------------------------------------------------------
        try:
            traffic = traffic_box['line-two'].split(',')
        except:
            pass
#----------------------------------------------------------------------------------------------
        try:
            traffic_date1 = traffic_box['months'].split(',')
            traffic_date = []
            for n in traffic_date1:
                an = n[1:-1].replace('"','')
                bn = an[:-2] + '20' + an[-2:]
                traffic_date.append(bn)
#             print(traffic_date)
        except:
            pass
#----------------------------------------------------------------------------------------------
        date = []
        
        try:
            dates = soup.findAll('table',attrs={'class':'Table Table--bordered'})[3].find('tbody').find_all('tr')
            for n in dates:
                date1 = n.find('th').find('strong').get_text()
                date1 = date1[:-2] + '20' + date1[-2:]
                date.insert(0,date1)
#             print(date)
        except:
            pass
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
        try:
            profits = f"{date[0]} : ${profit[0][1:].replace('null','0')}\n{date[1]} : ${profit[1].replace('null','0')}\n{date[2]} : ${profit[2].replace('null','0')}\n{date[3]} : ${profit[3].replace('null','0')}\n{date[4]} : ${profit[4].replace('null','0')}\n{date[5]} : ${profit[5].replace('null','0')}\n{date[6]} : ${profit[6].replace('null','0')}\n{date[7]} : ${profit[7].replace('null','0')}\n{date[8]} : ${profit[8].replace('null','0')}\n{date[9]} : ${profit[9].replace('null','0')}\n{date[10]} : ${profit[10].replace('null','0')}\n{date[11]} : ${profit[11][:-1].replace('null','0')}"
        except:
            profits = '-'
#         print(profits)
        
#----------------------------------------------------------------------------------------------       
        try:
            revenues = f"{date[0]} : ${revenue[0][1:].replace('null','0')}\n{date[1]} : ${revenue[1].replace('null','0')}\n{date[2]} : ${revenue[2].replace('null','0')}\n{date[3]} : ${revenue[3].replace('null','0')}\n{date[4]} : ${revenue[4].replace('null','0')}\n{date[5]} : ${revenue[5].replace('null','0')}\n{date[6]} : ${revenue[6].replace('null','0')}\n{date[7]} : ${revenue[7].replace('null','0')}\n{date[8]} : ${revenue[8].replace('null','0')}\n{date[9]} : ${revenue[9].replace('null','0')}\n{date[10]} : ${revenue[10].replace('null','0')}\n{date[11]} : ${revenue[11][:-1].replace('null','0')}"
        except:
            revenues = '-'
#         print(revenues)
#----------------------------------------------------------------------------------------------        
        try:
            traffics = f"{traffic_date[0][:]} : {traffic[0][1:]}\n{traffic_date[1]} : {traffic[1]}\n{traffic_date[2]} : {traffic[2]}\n{traffic_date[3]} : {traffic[3]}\n{traffic_date[4]} : {traffic[4]}\n{traffic_date[5]} : {traffic[5]}\n{traffic_date[6]} : {traffic[6]}\n{traffic_date[7]} : {traffic[7]}\n{traffic_date[8]} : {traffic[8]}\n{traffic_date[9]} : {traffic[9]}\n{traffic_date[10]} : {traffic[10]}\n{traffic_date[11][:]} : {traffic[11].split(']')[0]}"
        except:
            traffics = '-'
#         print(traffics)
        try:
            description = soup.find('div',attrs= {'class':'Listing-siteDescription'}).get_text()
        except:
            description = '-'
#         print(description)
       
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------   
        
        try:
            buy_now_price = soup.find('span',attrs= {'class':'Listing-buyItNowPrice'}).get_text().strip()
        except:
            buy_now_price = '-'
        
#----------------------------------------------------------------------------------------------       
        try:
            backlinks = soup.findAll('h3',attrs= {'class':'Semrush__attribute-value u-mgn-top-15'})[1].get_text()
        except:
            backlinks = '-'
       
#----------------------------------------------------------------------------------------------       
        try:
            reffering_domains = soup.findAll('h3',attrs= {'class':'Semrush__attribute-value u-mgn-top-15'})[0].get_text()
        except:
            reffering_domains = '-'
    
#----------------------------------------------------------------------------------------------
        channels = []
        try:
            channel = soup.findAll('table',attrs={'class':'Table Table--bordered'})[1].find('tbody').find_all('tr')
            for n in channel:
                date1 = n.find('td').get_text()
                channels.insert(0,date1)
            try:
                channel_1 = channels[-1].strip()
            except:
                channel_1 = '-'
            try:
                channel_2 = channels[-2].strip()
            except:
                channel_2 = '-'
            try:
                channel_3 = channels[-3].strip()
            except:
                channel_3 = '-'
            try:
                channel_4 = channels[-4].strip()
            except:
                channel_4 = '-'
            try:
                channel_5 = channels[-5].strip()
            except:
                channel_5 = '-'
        
        except:
            channel_1 = '-'
            channel_2 = '-'
            channel_3 = '-'
            channel_4 = '-'
            channel_5 = '-'
     
#----------------------------------------------------------------------------------------------
        countries = []
        try:
            country = soup.findAll('table',attrs={'class':'Table Table--bordered'})[2].find('tbody').find_all('tr')
            for n in country:
                date1 = n.find('td').get_text()
                countries.insert(0,date1)
                
            try:
                country_1 = countries[-1].strip()
            except:
                country_1 = '-'
            try:
                country_2 = countries[-2].strip()
            except:
                country_2 = '-'
            try:
                country_3 = countries[-3].strip()
            except:
                country_3 = '-'
            try:
                country_4 = countries[-4].strip()
            except:
                country_4 = '-'
            try:
                country_5 = countries[-5].strip()
            except:
                country_5 = '-'

          
        except:
            country_1 = '-'
            country_2 = '-'
            country_3 = '-'
            country_4 = '-'
            country_5 = '-'
#----------------------------------------------------------------------------------------------
        try:
            seller_name = soup.find('div',attrs= {'class':'about-the-seller__name'}).get_text().strip()
        except:
            seller_name = '-'
        try:
            total_keywords = soup.findAll('h3',attrs= {'class':'Semrush__attribute-value u-mgn-top-15'})[2].get_text()
        except:
            total_keywords = '-' 
 
        lists = {
            'Website': name,
            'Id': ids,
            'Url': link,
            'Domain': a1,
            'Platform': platform,
            'Industry':b1,
            'Country':c1,
            'Category':d1,
            'Monetization':e1,
            'Site Age': f1,
            'Avg net profit per Month $': g1,
            'Avg revenue per month': avg_rev_per_month,
            'Avg monthly traffic unique': h1,
            'Profit Months': profits,
            'Revenue Months': revenues,
            'Traffic Months': traffics,
            'Buy Now Price': buy_now_price,
            'Bid Price':i1,
            'Number of bids': j1,
            'About':description,
            'Backlinks Number': backlinks,
            'Reffering Domains': reffering_domains,
            'Total Keywords': total_keywords,
            'Top 1 channel': channel_1,
            'Top 2 channel': channel_2,
            'Top 3 channel': channel_3,
            'Top 4 channel': channel_4,
            'Top 5 channel': channel_5,
            'Top 1 Countries': country_1,
            'Top 2 countries': country_2,
            'Top 3 countries': country_3,
            'Top 4 countries': country_4,
            'Top 5 countries': country_5,
            'Seller Name': seller_name,
            'Country of Seller':c1,
            'Date/Time Scraped': date_time
        }
        data.append(lists)
#         print(data)
df1 = pd.DataFrame(data)
df = df1.drop_duplicates(subset=['Domain', 'Bid Price', 'Seller Name','Backlinks Number'], keep=False).reset_index(drop=True)
df.to_csv(f'Flippa_{date_time1}.csv',encoding='utf-8-sig', index=False)
#----------------------------------------------------------------------------------------------