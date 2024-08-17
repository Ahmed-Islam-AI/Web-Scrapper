import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    
}


base_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=mobile+phones&_sacat=0&_pgn="

# page number 
page_num = 1

Names =[]
Brands = []
Price = []
Shipping_Cost = []
Location = []
View_by = []
Links =[]


# we can use for multiple pages
#while True:

#for specific range pages we can use for loop
for i in range(1,3):
    # concatinating the page number with the initial base url
    url = base_url + str(page_num)
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        #print("Success")
        # Access the html of the whole page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        data = soup.find_all('div',{"class":'s-item__info clearfix'})
        #print(len(data))
        
        for item in data[2:]:
            try:
                name = item.find('div',{"class":"s-item__title"}).text.strip()          
                #print(name)
                Names.append(name)
                
        
            except:
                Names.append("")
                
            
            try:
                brands = item.find('div',{"class": "s-item_subtitle"}).text.strip()
                #print(brands)
                Brands.append(brands)
                
            except:
                Brands.append("")
                
                
            try:
                price = item.find('span',{"class":"s-item__price"}).text.strip()
                #print(price)
                Price.append(price)
                
            except:
                Price.append("")
                
            try:
                shipping_cost = item.find('span', {"class": "s-item__shipping s-item__logisticsCost"}).text.strip()
                #print(shipping_cost)
                Shipping_Cost.append(shipping_cost)
            except:
                Shipping_Cost.append("")
                
            try:
                location = item.find("span", {"class": "s-item__location s-item__itemLocation"}).text.strip()
                #print(location)
                Location.append(location)
                
            except:
                Location.append("")
                
            try:
                views = item.find('span', {"class": "s-item__dynamic s-item__watchCountTotal"}).text.strip()
                #print(views)
                View_by.append(views)
                
            except:
                View_by.append("")
                
            try:
                link = item.find('a')['href']
                #print(link)
                Links.append(link)
            except:
                Links.append("")
         
         
        # loop through for the next page        
        next_page = soup.find('a', {"class": "pagination__next icon-link"})
        
        if next_page:
            page_num += 1
            time.sleep(2)
        else:
            break
    else:
        break
    
                
    
    
    
    
# making a CSV file by using pandas dataframe
pd.DataFrame({
    'Name': Names,
    'Brand': Brands,
    'Price': Price,
    'Shipping_Cost': Shipping_Cost,
    'Location': Location,
    'Views': View_by,
    'Link': Links
}).to_csv("ebay.csv", index=False)