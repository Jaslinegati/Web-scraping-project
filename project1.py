#import necessary liraries
#pip install beautifulsoup4
import requests
import csv
from bs4 import BeautifulSoup

#define url of product page
url='https://www.amazon.co.uk/s?k=kitchenware&crid=Y90QIIHMP13C&sprefix=%2Caps%2C62&ref=nb_sb_ss_recent_1_0_recent'

#send get request to the url n receive html content
response = requests.get(url)
html = response.text

#create a beautifulsoup object to parse the html
soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())

# test = soup.find_all('span', class_='a-size-base-plus a-color-base a-text-normal')
# print(test)

card_class = 's-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border'
card_class_2 = 'sg-col-inner'
result_cards = soup.find_all('div', class_=card_class)
data = []

for card in result_cards:
    # print(card)
    title = card.find('span', class_='a-size-base-plus a-color-base a-text-normal').get_text().strip()
    # print(title)
    raw_price = card.find('span', class_='a-offscreen')
    # print(raw_price)
    
    if(raw_price is None):
        continue
    else:
        price = raw_price.get_text().strip()
        print(price)
        
        #append data to a tupule
        data.append((title, price))

# print(f"{data=}")


# Save data to csv
# filename='data.csv'

# with open(filename, 'w', newline='') as csvfile:
#     # Creating a CSV dict writer object
#     writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())

#     # Writing headers (field names)
#     writer.writeheader()

#     # Writing data rows
#     for row in data:
#         writer.writerow(row)
        
# print(f"Data written to {filename}")

# Import the 'mysql-connector-python library and create 
# a connection to the mysql server by specifying the host, user, password and db

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user= "Project_1",
    password= "1lovevans@!",
    database = "Proj1_db"
)

#Create a cursor object to interact with the database
cursor = mydb.cursor()   

#data = [tuple(d.values()) for d in data]

# use re module to extract only the numeric part of the string and then convert it to float.

query = "INSERT INTO Goods (Title, Price) VALUES (%s, %s)"


#insert rows into the database
for item in data:
    print(data)
    import re
    price = re.findall(r"\d+\.\d", item[1])
    price_float = float(price[0])
    # print(f'{item=}')
    cursor.execute(query, (item[0], price_float))
    mydb.commit()

# cursor.execute(query, *item)

cursor.close()
mydb.close()