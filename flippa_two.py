import pandas as pd                                   
from bs4 import BeautifulSoup                          
import requests  

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

df = pd.read_csv('flippa.csv')

all_links_collected_to_csv = df['Listing_url'].tolist()
domain = df['Domain'].tolist()
type = df['Type'].tolist()
country_a = df['Country'].tolist()
category = df['Category'].tolist()
monetization = df['Monetization'].tolist()
site_age = df['Site Age'].tolist()
avg_net_profit_per_month = df['Avg net profit per month $'].tolist()
avg_monthly_traffic_unique = df['Avg monthly traffic unique'].tolist()
bid_price = df['Bid price $'].tolist()
number_of_bids = df['Number of bids'].tolist()
about = df['About'].tolist()



with requests.Session() as s:
    url = 'https://www.flippa.com/sign-in'
    r = s.get(url, headers = headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    login_data['authenticity_token'] = soup.find('input', attrs = {'name':'authenticity_token'})['value']
    
    r = s.post(url, data = login_data, headers = headers)
    data = []
    list = {}
    counts = 0
    name = 'Flippa'
    for link,a,b,c,d,e,f,g,h,i,j,k in zip(all_links_collected_to_csv,domain,type,country_a,category,monetization,site_age,avg_net_profit_per_month,avg_monthly_traffic_unique,bid_price,number_of_bids,about):
        counts += 1
        print(counts)
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
            avg_rev_per_month = soup.find('div',attrs= {'id':'gross_revenue'}).get_text().strip()
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
                traffic_date.append(n[1:-1])
        except:
            pass
#----------------------------------------------------------------------------------------------
        date = []
        
        try:
            dates = soup.findAll('table',attrs={'class':'Table Table--bordered'})[3].find('tbody').find_all('tr')
            for n in dates:
                date1 = n.find('th').find('strong').get_text()
                date.insert(0,date1)
        except:
            pass
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
        try:
            profits = f"${profit[0][1:]} {date[0]}\n${profit[1]} {date[1]}\n${profit[2]} {date[2]}\n${profit[3]} {date[3]}\n${profit[4]} {date[4]}\n${profit[5]} {date[5]}\n${profit[6]} {date[6]}\n${profit[7]} {date[7]}\n${profit[8]} {date[8]}\n${profit[9]} {date[9]}\n${profit[10]} {date[10]}\n${profit[11].split(']')[0]} {date[11]}"
        except:
            profits = '-'
        
#----------------------------------------------------------------------------------------------       
        try:
            revenues = f"${revenue[0][1:]} {date[0]}\n${revenue[1]} {date[1]}\n${revenue[2]} {date[2]}\n${revenue[3]} {date[3]}\n${revenue[4]} {date[4]}\n${revenue[5]} {date[5]}\n${revenue[6]} {date[6]}\n${revenue[7]} {date[7]}\n${revenue[8]} {date[8]}\n${revenue[9]} {date[9]}\n${revenue[10]} {date[10]}\n${revenue[11].split(']')[0]} {date[11]}"
        except:
            revenues = '-'
       
#----------------------------------------------------------------------------------------------        
        try:
            traffics = f"{traffic[0][1:]} {traffic_date[0][1:]}\n{traffic[1]} {traffic_date[1]}\n{traffic[2]} {traffic_date[2]}\n{traffic[3]} {traffic_date[3]}\n{traffic[4]} {traffic_date[4]}\n{traffic[5]} {traffic_date[5]}\n{traffic[6]} {traffic_date[6]}\n{traffic[7]} {traffic_date[7]}\n{traffic[8]} {traffic_date[8]}\n{traffic[9]} {traffic_date[9]}\n{traffic[10]} {traffic_date[10]}\n{traffic[11].split(']')[0]} {traffic_date[11][:-1]}"
        except:
            traffics = '-'
       
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
            channel_1 = channels[-1].strip()
            channel_2 = channels[-2].strip()
            channel_3 = channels[-3].strip()
        
        except:
            channel_1='-'
            channel_2 = '-'
            channel_3 = '-'
     
#----------------------------------------------------------------------------------------------
        countries = []
        try:
            country = soup.findAll('table',attrs={'class':'Table Table--bordered'})[2].find('tbody').find_all('tr')
            for n in country:
                date1 = n.find('td').get_text()
                countries.insert(0,date1)
            country_1 = countries[-1].strip()
            country_2 = countries[-2].strip()
            country_3 = countries[-3].strip()
          
        except:
            pass
#----------------------------------------------------------------------------------------------
        try:
            seller_name = soup.find('div',attrs= {'class':'about-the-seller__name'}).get_text().strip()
        except:
            seller_name = '-' 
 
        list = {
            'Website': name,
            'Id': counts,
            'url': link,
            'Domain': a,
            'Platform': platform,
            'Type':b,
            'Country':c,
            'Category':d,
            'Monetization':e,
            'Site Age': f,
            'Avg net profit per Month $': g,
            'Avg revenue per month': avg_rev_per_month,
            'Avg monthly traffic unique': h,
            'Profit with Months': profits,
            'Revenue with Months': revenues,
            'High Unique Traffic with month': traffics,
            'Buy Now Price': buy_now_price,
            'Bid Price':i,
            'Number of bids': j,
            'About':k,
            'Backlinks Number': backlinks,
            'Reffering Domains': reffering_domains,
            'Top 1 channel': channel_1,
            'Top 2 channel': channel_2,
            'Top 3 channel': channel_3,
            'Top 1 Countries': country_1,
            'Top 2 countries': country_2,
            'Top 3 countries': country_3,
            'Seller Name': seller_name
        }
        data.append(list)
    df = pd.DataFrame(data)
    df.to_csv('Final_flippa.csv',encoding='utf-8-sig')
#----------------------------------------------------------------------------------------------