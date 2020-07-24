from bs4 import BeautifulSoup as bsoup
import requests
import time
import copy
import pandas as pd
import re

#from bson.objectid import ObjectId

# connect to the hosted MongoDB instance

#Load webpage content 
def carguru_call(zip,page_num):
    page = requests.get('https://www.cars.com/for-sale/searchresults.action/?page='+str(page_num)+'&perPage=100&rd=20&searchSource=PAGINATION&sort=relevance&zc='+str(zip))

    #
    #convert to a beautiful soup object:
    soup = bsoup(page.content, features="lxml")
    #show contents
    soup.prettify()

    # auto tempest isn't working.. did they somehow make everything private? D:
    #start scraping find and find_all
    body = soup.find_all('script')
    
    #body = soup.find('class')
    #body = soup.find('div' )
    # yes or no answer if it is certified pre-owned
    #spec = body.find_all('span')
    return str(body)
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
    counter = 0
    while counter < num:
        car = car_organized(zip)
        if car not in car_list:
            counter +=1
            car_list.append(car)
    return car_list

def populate_car_list(zip,page_num):
    with open('./carlist_losA.csv','a') as f:
        for item in organize_list_cars(zip,page_num):
            f.write("%s\n" % item)
    pass
   
zip_codes_data = pd.read_csv('los_angles_zipcode.csv')
zips = zip_codes_data['zip'].to_numpy()
    

def populate_csv(lst, num):
    for i in lst:
        populate_car_list(i, num)
    pass

def organize_list_cars(zip, page_num):
    delimeters = '"type"'
    strings = carguru_call(zip, page_num)
    lstin = re.split(delimeters, strings)
    #shorttening list of stuff :0
    new_list = []
    for i in lstin:
        if i.startswith('' ':"inventory"') == True:
            new_list.append(i)

    price = []
    make =[]
    model = []
    year = []
    bodyStyle = []
    sellerRating = []
    city = []
    state = []
    mileage = []
    
    #populate make
    for i in new_list:
        make.append(re.findall('"make":"(.+)","makeId"', i))
        model.append((re.findall('"model":"(.+)","modelId"', i)))
        year.append((re.findall('"year":(.+),"trim"', i)))
        bodyStyle.append((re.findall('"bodyStyle":"(.+)","customerId"', i)))
        sellerRating.append((re.findall(',"rating":(.+),"reviewCount"', i)))
        city.append((re.findall('"city":"(.+),"state":', i)))
        price.append((re.findall(',"price":(.+),"mileage":', i)))
        mileage.append((re.findall(',"mileage:"(.+),"vin":', i)))
        state.append((re.findall(',"state":"(.+)","truncatedDescription', i)))
    masterlist = []
    for i in range(len(make)):
        masterlist.append(str(price[i]) + str(make[i]) + str(model[i]) + str(year[i]) + str(bodyStyle[i]) + str(sellerRating[i])+str(city[i])+str(state[i])+str(mileage[i]))

    container = []
    for i in range(len(masterlist)):
        cars = masterlist[i]
        cars = cars.replace('[]', ',None')
        cars = cars.replace('[', '')
        cars = cars.replace(']', '')
        cars = cars.replace("''",',')
        cars = cars.replace("'", '')
        cars = cars.replace('"','')
        container.append(cars)


    return container
for zi in zips:
    for a in range(1,11):
        populate_car_list(zi,a)
