from bs4 import BeautifulSoup as bsoup
import requests
import time
import copy
import pandas as pd

#from bson.objectid import ObjectId

# connect to the hosted MongoDB instance

#Load webpage content 
def carguru_call(zip):
    r = requests.get('https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=&zip='+str(zip))

    #convert to a beautiful soup object:
    soup = bsoup(r.content, features='lxml')
    #show contents
    soup.prettify()

    # auto tempest isn't working.. did they somehow make everything private? D:
    #start scraping find and find_all
    #titles = soup.find_all('class', attrs = {'class': 'price-wrap'})

    body = soup.find('h4')
    # yes or no answer if it is certified pre-owned
    spec = body.find_all('span')
    return spec
def car_organized(zip):
    
    
    cars = [c.string for c in carguru_call(zip)]
    details2 = cars[0].replace(' for sale -', ',')
    details2 = details2.replace('Used ','')
    details2 = details2.replace(' - ', ', ')
    details2 = details2.replace(' with', ',')
    details2 = details2[:4] + ',' + details2[4:]  
    cars[0] = details2

    return cars

def car_list(zip,num):
    car_list= []
    for _ in range(num):
        car_list.append(car_organized(zip))
        #time.sleep(.2)
    return car_list

def populate_car_list(zip,num):
    with open('./carlist.csv','a') as f:
        for item in car_list(zip,num):
            f.write("%s\n" % item)
    pass
   
zip_codes_data = pd.read_csv('zip_code_database.csv')
zips = zip_codes_data['zip'].to_numpy()
    

def populate_csv(lst, num):
    for i in lst:
        populate_car_list(i, num)
    pass


for i in zips:
    if int(i) > 10000:
        populate_car_list(int(i),10)

