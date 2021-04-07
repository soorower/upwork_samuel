import pandas as pd                                   
from bs4 import BeautifulSoup                          
import requests  
import datetime
from time import sleep
import json
import random
from itertools import cycle
import traceback

# headers = {
#     'Access-Control-Allow-Origin': '*',
#     'Access-Control-Allow-Methods': 'GET',
#     'Access-Control-Allow-Headers': 'Content-Type',
#     'Access-Control-Max-Age': '3600',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'
# }
df = pd.read_excel('exchange_all_listings_today.xlsx')
all_links = df['links'].tolist()
print(len(all_links))

x = datetime.datetime.now()
hour = x.hour
minute = x.minute
date_1= x.day
month = x.month
year = x.year
date_time1 = f'{date_1}-{month}-{year}_{hour}-{minute}'
date_time = f'{date_1}-{month}-{year} {hour}:{minute}'
data = []
list = {}
counts = 0
name = 'Exchange'

try:
    for link in all_links:
        user_agent_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.749 Yowser/2.5 Safari/537.36'
        ]
        user_agent = random.choice(user_agent_list)

        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': user_agent
        }
        counts += 1
        print(counts)
        try:
            rs = requests.get(link, headers= headers)
            soup = BeautifulSoup(rs.content, 'html.parser')
        except:
            pass
        sleep(2)
    #     print(rs.content)
    #-------------------------------------------------------------------------------------------------------------------------------

        try:
            ids = int(soup.find('h1',attrs= {'class':'_3c7Mo _3Rk8c _1-Yji'}).get_text().split('#')[1])
        except:
            ids = 'Not Found'

    #     print(ids)
    #-------------------------------------------------------------------------------------------------------------------------------    
        try:
            try:
                domain = soup.find('a',attrs= {'class':'_2gej5 _3dg_f _3c7Mo GbPX0 _1-Yji'}).get('href')
                if 'https' in domain:
                    pass
                elif 'URL Hidden' in domain:
                    pass
                else:
                    domain = '-'
            except:
                domain = soup.find('span',attrs= {'class':'_3c7Mo _1-Yji'}).get_text().strip()
                if 'https' in domain:
                    pass
                elif 'URL Hidden' in domain:
                    pass
                else:
                    domain = '-'
    #         print(domain)
        except:
            domain='-'
        print(domain)

    #-------------------------------------------------------------------------------------------------------------------------------    

        platform = 'Shopify'


        try: 
            category = soup.find('a',attrs= {'class':'_3vKm9 jmdHf'}).get_text().strip()
        except:
            category = '-'
    #-------------------------------------------------------------------------------------------------------------------------------    

        try:
            monitization = soup.findAll('div',attrs= {'class':'_2ONvs _2vj1S _33wM-'})[2].findAll('span')[1].get_text().replace('"',' ').strip()
        except:
            monitization = '-'
    #     print(monitization)
    #-------------------------------------------------------------------------------------------------------------------------------    

        try: 
            site_age = soup.find('div',attrs= {'class':'_2ONvs _2vj1S _33wM-'}).findAll('span')[1].get_text().replace('"',' ').strip()
        except:
            site_age = '-'
    #     print(site_age)

    #-------------------------------------------------------------------------------------------------------------------------------    

        try:
            avg_prof_month = soup.findAll('div',attrs= {'class':'_1uCwB LcAyu'})[1].findAll('span')[1].get_text().replace('"',' ').strip()
        except:
            avg_prof_month = '-'
    #     print(avg_prof_month)
    #-------------------------------------------------------------------------------------------------------------------------------    

        try:
            avg_rev_month = soup.findAll('div',attrs= {'class':'_1uCwB LcAyu'})[0].findAll('span')[1].get_text().replace('"',' ').strip()
        except:
            avg_rev_month = '-'
    #     print(avg_rev_month)
    #-------------------------------------------------------------------------------------------------------------------------------    

        try:
            avg_traffic_month = soup.findAll('li',attrs= {'class':'_2v9K-'})[1].findAll('span')[2].get_text().replace('"',' ').strip()
        except:
            avg_traffic_month = '-'
    #     print(avg_traffic_month)
    #-------------------------------------------------------------------------------------------------------------------------------    

        try:
            bid_price1 = soup.findAll('span',attrs = {'class':'_3sxJP'})[1].get_text().strip()
            bid_price = f'${bid_price1} USD'
        except:
            bid_price = '-'
    #     print(bid_price)
    #-------------------------------------------------------------------------------------------------------------------------------    

        try:
            about1 = soup.findAll('div',attrs={'class':'_1beKW'})
            about2 = []
            for ab in about1:
                title = ab.find('h3',attrs={'class':'_3c7Mo _149MA _1-Yji'}).get_text()
                descrip = ab.find('div',attrs={'class':'long-form-content'}).get_text()
                about2.append(f'{title}: \n{descrip}')
            about = f'{about2[0]}\n{about2[1]}\n{about2[2]}\n{about2[3]}\n{about2[4]}'
    #         print(about)

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
            time_to_run = soup.findAll('div',attrs= {'class':'_2ONvs _2vj1S _33wM-'})[1].findAll('span')[1].get_text().replace('"',' ').strip().replace('approximately',' ')
        except:
            time_to_run='-'
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
            avg_sale_month = '-'
    #     print(avg_sale_month)
    #-------------------------------------------------------------------------------------------------------------------------------    

        try:
            total_revenue1 = soup.findAll('div',attrs={'class':'_1uCwB LcAyu'})[4].get_text()
            total_revenue = f'{total_revenue1} USD'
        except:
            total_revenue = '-'
    #     print(total_revenue)
    #-------------------------------------------------------------------------------------------------------------------------------    

        try:
            total_traffic = soup.findAll('span',attrs={'class':'_3Gxwk'})[4].get_text().strip().replace('Visits',' ')

        except:
            total_traffic = '-'
    #     print(total_traffic)
    #-------------------------------------------------------------------------------------------------------------------------------    

        try:
            mailing_list = soup.findAll('span',attrs={'class':'_3Gxwk'})[5].get_text().strip().replace('subscribers',' ')

        except:
            mailing_list = '-'
    #     print(mailing_list)
    #-------------------------------------------------------------------------------------------------------------------------------    

        try:
            expence = []
            try:
                expences = soup.find('ul',attrs = {'class':'_2UlBf'}).findAll('li')
                for e in expences:
                    a = e.find('dt').get_text()
                    b= e.find('dd').get_text()
                    expence1 = f'{a} - {b}'
                    expence.append(expence1)
                e_1 = expence[0]
                e_2 = expence[1]
                e_3 = expence[2]
            except:
                expences = soup.find('ul',attrs = {'class':'_2UlBf'}).find('li')
                a = expences.find('dt').get_text()
                b= expences.find('dd').get_text()
                expence1 = f'{a} - {b}'
                expence.append(expence1)
                e_1 = expence[0]
                e_2 = '-'
                e_3 = '-'



        except:
            e_1 = '-'
            e_2 = '-'
            e_3 = '-'
            pass
    #     sleep(1)
    #-------------------------------------------------------------------------------------------------------------------------------    
        try:
            jsons = soup.findAll('script',attrs={'type':'application/json'})[1].get_text()[4:-3]
            m = json.loads(jsons)
            with open('data_exchange.json', 'w') as outfile:
                json.dump(m, outfile)
            sleep(1)
            with open('data_exchange.json','r') as file:
                datas = json.load(file)
        except:
            pass
    #     print(datas)
    #     sleep(1)
        try:
            date_with_rev = []
            date_rev = datas.get('shop').get('monthByMonthRevenue')
            for i in date_rev:
                date1 = i.get('date')[:-3][:-3]
                date2 = i.get('date')[:-3][-2:].replace('01','Jan').replace('02','Feb').replace('03','Mar').replace('04','Apr').replace('05','May').replace('06','Jun').replace('07','Jul').replace('08','Aug').replace('09','Sep').replace('10','Oct').replace('11','Nov').replace('12','Dec')
                date = f'{date2} {date1}'
                rev = i.get('revenue')
                date_revenue = f'{date} : ${rev}'
                date_with_rev.append(date_revenue)
            revenues = f'{date_with_rev[-1]}\n{date_with_rev[-2]}\n{date_with_rev[-3]}\n{date_with_rev[-4]}\n{date_with_rev[-5]}\n{date_with_rev[-6]}'
        except:
            revenues = '-'
    #     print(revenues)
        try:
            date_with_traf = []
            date_traf = datas.get('shop').get('monthByMonthTraffic')
            for i in date_traf:
                date1 = i.get('date')[:-3][:-3]
                date2 = i.get('date')[:-3][-2:].replace('01','Jan').replace('02','Feb').replace('03','Mar').replace('04','Apr').replace('05','May').replace('06','Jun').replace('07','Jul').replace('08','Aug').replace('09','Sep').replace('10','Oct').replace('11','Nov').replace('12','Dec')
                date = f'{date2} {date1}'
                traf = i.get('traffic')
                date_traffic = f'{date} : {traf}'
                date_with_traf.append(date_traffic)
            traffics = f'{date_with_traf[-1]}\n{date_with_traf[-2]}\n{date_with_traf[-3]}\n{date_with_traf[-4]}\n{date_with_traf[-5]}\n{date_with_traf[-6]}'
        except:
            traffics = '-'
    #     print(traffics)
    #-------------------------------------------------------------------------------------------------------------------------------    

    #     sleep(1)

        list = {
            'Website': name,
            'Id': ids,
            'Url': link,
            'Domain': domain,
            'Platform': platform,
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
            'Seller Name': seller_name,
            'Date/Time Scraped': date_time
        }
        data.append(list)
except:
    pass
df1 = pd.DataFrame(data)
df = df1.drop_duplicates(subset=['Domain', 'Bid Price', 'Seller Name'], keep=False).reset_index(drop=True)
df.to_csv(f'Exchange_{date_time1}.csv',encoding='utf-8', index=False)

print('Done!')