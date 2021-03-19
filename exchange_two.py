import pandas as pd                                   
from bs4 import BeautifulSoup                          
import requests  
import datetime
from time import sleep
import json
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Safari/537.36'
}

df = pd.read_excel('exchange_all_listings.xlsx')
all_links = df['links'].tolist()[:1]
# print(all_links)

data = []
list = {}
counts = 0
name = 'Exchange'
for link in all_links:
    counts += 1
    print(counts)
    rs = requests.get(link, headers= headers)
    soup = BeautifulSoup(rs.content, 'html.parser')
    sleep(1)
#     print(rs.content)
#-------------------------------------------------------------------------------------------------------------------------------
    try:
        ids = soup.find('h1',attrs= {'class':'_3c7Mo _3Rk8c _1-Yji'}).get_text().strip().split('#')[1]
    except:
        ids = soup.find('h1',attrs= {'class':'_3c7Mo _3Rk8c _1-Yji'}).get_text().strip()
#     print(ids)
#-------------------------------------------------------------------------------------------------------------------------------    
    
    try:
        domain = soup.find('a',attrs= {'class':'_2gej5 _3dg_f _3c7Mo GbPX0 _1-Yji'}).get_text().strip()
    except:
        domain = soup.find('span',attrs= {'class':'_3c7Mo _1-Yji'}).get_text().strip()
#     print(domain)  
        
#-------------------------------------------------------------------------------------------------------------------------------    
    
    platform = 'Shopify'
#   platform = soup.find('div',attrs= {'id':'platform'}).get_text().strip()
#     print(platform)
    
    industry = '-'
#     print(industry)

    country = 'null'
    
    try: 
        category = soup.find('a',attrs= {'class':'_3vKm9 jmdHf'}).get_text().strip()
    except:
        category = '-'
        pass
#-------------------------------------------------------------------------------------------------------------------------------    
    
    try:
        monitization = soup.findAll('div',attrs= {'class':'_2ONvs _2vj1S _33wM-'})[2].findAll('span')[1].get_text().replace('"',' ').strip()
    except:
        pass
#     print(monitization)
#-------------------------------------------------------------------------------------------------------------------------------    
  
    try: 
        site_age = soup.find('div',attrs= {'class':'_2ONvs _2vj1S _33wM-'}).findAll('span')[1].get_text().replace('"',' ').strip()
    except:
        pass
#     print(site_age)
    
#-------------------------------------------------------------------------------------------------------------------------------    
 
    try:
        avg_prof_month = soup.findAll('div',attrs= {'class':'_1uCwB LcAyu'})[1].findAll('span')[1].get_text().replace('"',' ').strip()
    except:
        pass
#     print(avg_prof_month)
#-------------------------------------------------------------------------------------------------------------------------------    
 
    try:
        avg_rev_month = soup.findAll('div',attrs= {'class':'_1uCwB LcAyu'})[0].findAll('span')[1].get_text().replace('"',' ').strip()
    except:
        pass
#     print(avg_rev_month)
#-------------------------------------------------------------------------------------------------------------------------------    

    try:
        avg_traffic_month = soup.findAll('li',attrs= {'class':'_2v9K-'})[1].findAll('span')[2].get_text().replace('"',' ').strip()
    except:
        pass
#     print(avg_traffic_month)
#-------------------------------------------------------------------------------------------------------------------------------    
 
    try:
        bid_price = soup.findAll('span',attrs = {'class':'_3sxJP'})[1].get_text().strip()
        bid_price = f'${bid_price}'
    except:
        bid_price = '-'
        pass
#     print(bid_price)
#-------------------------------------------------------------------------------------------------------------------------------    

    try:
        about = soup.find('section',attrs= {'id':'BusinessStory'}).get_text().strip()
    except:
        about = '-'
#     print(about)
#-------------------------------------------------------------------------------------------------------------------------------    
 
    try:
        seller_name = soup.find('span',attrs= {'class':'_2a41F _3c7Mo _149MA _1-Yji spVWc'}).get_text()
    except:
        seller_name = '-'
#     print(seller_name)
#-------------------------------------------------------------------------------------------------------------------------------    

    try: 
        time_to_run = soup.findAll('div',attrs= {'class':'_2ONvs _2vj1S _33wM-'})[1].findAll('span')[1].get_text().replace('"',' ').strip()
    except:
        time_to_run='-'
        pass
#     print(time_to_run)
#-------------------------------------------------------------------------------------------------------------------------------    
  
    try:
        profit_margin = soup.findAll('span',attrs={'class':'_3Gxwk'})[2].get_text().strip()
        
    except:
        profit_margin = '-'
#     print(profit_margin)
#-------------------------------------------------------------------------------------------------------------------------------    
    
    try:
        avg_sale_month = soup.findAll('span',attrs={'class':'_3Gxwk'})[3].get_text().strip()
    except:
        profit_margin = '-'
#     print(avg_sale_month)
#-------------------------------------------------------------------------------------------------------------------------------    
  
    try:
        total_revenue = soup.findAll('div',attrs={'class':'_1uCwB LcAyu'})[4].get_text()
    except:
        total_revenue = '-'
#     print(total_revenue)
#-------------------------------------------------------------------------------------------------------------------------------    
      
    try:
        total_traffic = soup.findAll('span',attrs={'class':'_3Gxwk'})[4].get_text().strip()
        
    except:
        total_traffic = '-'
#     print(total_traffic)
#-------------------------------------------------------------------------------------------------------------------------------    
  
    try:
        mailing_list = soup.findAll('span',attrs={'class':'_3Gxwk'})[5].get_text().strip()
        
    except:
        mailing_list = '-'
#     print(mailing_list)
#-------------------------------------------------------------------------------------------------------------------------------    
  
    try:
        expences = soup.find('ul',attrs={'class':'_2UlBf'}).findAll('li')
        expence = []
        for e in expences:
            a = e.find('dt').get_text()
            b= e.find('dd').get_text()
            expence1 = f'{a} - {b}'
            expence.append(expence1)
#         print(expence)
        e_1 = expence[1]
        e_2 = expence[2]
        e_3 = expence[3]
      
    except:
        e_1 = '-'
        e_2 = '-'
        e_3 = '-'
        pass
#-------------------------------------------------------------------------------------------------------------------------------    
    jsons = soup.findAll('script',attrs={'type':'application/json'})[1].get_text()[4:-3]
    m = json.loads(jsons)
    with open('data_exchange.json', 'w') as outfile:
        json.dump(m, outfile)
    with open('data_exchange.json','r') as file:
        datas = json.load(file)
    

    try:
        date_with_rev = []
        date_rev = datas.get('shop').get('monthByMonthRevenue')
        for i in date_rev:
            date = i.get('date')
            rev = i.get('revenue')
            date_revenue = f'{date} : ${rev}'
            date_with_rev.append(date_revenue)
        revenues = f'{date_with_rev[0]}\n{date_with_rev[1]}\n{date_with_rev[2]}\n{date_with_rev[3]}\n{date_with_rev[4]}\n{date_with_rev[5]}\n{date_with_rev[6]}\n{date_with_rev[7]}\n{date_with_rev[8]}\n{date_with_rev[9]}\n{date_with_rev[10]}\n{date_with_rev[11]}'
    except:
        revenues = '-'
#     print(revenues)
    try:
        date_with_traf = []
        date_traf = datas.get('shop').get('monthByMonthTraffic')
        for i in date_traf:
            date = i.get('date')
            traf = i.get('traffic')
            date_traffic = f'{date} : {traf}'
            date_with_traf.append(date_traffic)
        traffics = f'{date_with_traf[0]}\n{date_with_traf[1]}\n{date_with_traf[2]}\n{date_with_traf[3]}\n{date_with_traf[4]}\n{date_with_traf[5]}\n{date_with_traf[6]}\n{date_with_traf[7]}\n{date_with_traf[8]}\n{date_with_traf[9]}\n{date_with_traf[10]}\n{date_with_traf[11]}'
    except:
        traffics = '-'
        
#-------------------------------------------------------------------------------------------------------------------------------    
       
    sleep(4)
        
    list = {
        'Website': name,
        'Id': ids,
        'Url': link,
        'Domain': domain,
        'Platform': platform,
        'Industry':industry,
        'Country':country,
        'Category':category,
        'Monetization':monitization,
        'Site Age': site_age,
        'profit_margin': profit_margin,
        'Avg sale p/m': avg_sale_month,
        'Total Revenue': total_revenue,
        'Total Traffic': total_traffic,
        'Total Mailing List': mailing_list,
        'Time to run the bussiness': time_to_run,
        'Avg net profit per Month $': avg_prof_month,
        'Avg net revenue per Month $': avg_rev_month,
        'Avg monthly traffic unique': avg_traffic_month,
        'Revenue Months': revenues,
        'Traffic Months': traffics,
        'Bid Price':bid_price,
        'About':about,
        'Expences 1': e_1,
        'Expences 2': e_2,
        'Expences 3': e_3,
        'Seller Name': seller_name
    }
    data.append(list)
df = pd.DataFrame(data)
df.to_csv('Final_exchange.csv',encoding='utf-8', index=False)