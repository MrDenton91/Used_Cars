# CapStone Project 1
July 20, 2020
  - current python code has 10 car, (1 page), limit per unique zip code in the US.
    + There is a parameter that can adjust the number of unique cars from each zip code,
        but given the time frame for presenting This is the choice that makes amount of sense.
    + Reminder: valid zipcodes are uniqu 5-digit numbers,(technically 7-digit), for the site that 
        I'm scraping from it doesn't like 7-digit zipcodes for some entries.
    + current code produces 11k results every 4 hours.
        -About 2750 every hour.
    + data collected: 
        - zipcode, year, make/model, price, milage,alloy wheels, Bluetooth, Back-up camera, certified pre-owned, remote       
          start, leather seats, sunroof/moonroof, 'Special' package, transmision type, color


July 21, 2020
  - Given the time frame of this project, I was adviced to focus my search more towards Los Angels, New York, and Chicago.
    + I created 3 seperate scraping programs for each city, and I ran them in parrel. 
      ~ I ran into may issues, one scraper wasn't populating a csv file, simply running them sepeartly in seperate terminals          wasn't working for some reason. I had to run one scraper in VScode and the other two in terminal, this took a some 
         time to trouble shoot. Than I kept losing internet access, as you can imagine I had to find whereit left off
         and restart the scraping.
         ~ This didn't leave me time to contimplate what would be intersting to look at. 


July 22, 2020
  - Data was collected on Los Angeles, Chicago, and New York city areas. Random sampleing was collected in a 100 mile radius, with 100 samples being collected at each zipcode.
  - Fast facts: 
    + around 40.8 million used cars were sold in 2019, 
    + on average a zip-code covers 82.25 sq miles,
        ~ I expect some repeats in my data.
        ~ Chicago is about 234 sqr/miles
        ~ Los Angeles is about 503 sqr/miles
        ~ New York is about 302 sqr/miles
     
        
      
