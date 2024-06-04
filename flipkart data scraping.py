import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Ratings = []

for i in range(2,5):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url) 

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="DOjaWF gdgoEp")
    
    #scraping data 

    names = box.findAll("div", class_="KzDlHZ")
    for i in names:
        name = i.text
        Product_name.append(name)

    prices = box.findAll("div", class_="Nx9bqj _4b5DiR")
    for i in prices:
        name = i.text
        Prices.append(name)
    
    description = box.findAll("ul", class_="G4BRas")
    for i in description:
        name = i.text
        Description.append(name)
    
    ratings = box.findAll("div", class_="XQDdHH")
    for i in ratings:
        name = i.text
        Ratings.append(name)

#making a data frame

df = pd.DataFrame({"Product Name":Product_name, "Prices":Prices,"Description":Description,"Ratings":Ratings})

df.to_csv("C:/Users/Chetan/Documents/Python Data Analytics/flipkart_mobiles_under_50k.csv")
    




    