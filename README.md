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
      ~ I ran into may issues, one scraper wasn't populating a csv file, simply running them sepeartly in seperate terminals          
        wasn't working for some reason. I had to run one scraper in VScode and the other two in terminal, this took a some 
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
        
        
July 23, 2020
  - I had a medical emergency yesterday, I was about halfway through cleaning my data.
  - I moved my data cleaning fuctions over to a jupyter notebook, to make things go faster.
  
  - It's about 6:30pm... I just realised that most, 98%, of the data collected was repeats.. ( ended up sleeping at 1:30am )
      + The variable that I was scarping was actualy the highly 'recommended', or advertised, car.
          ~ further questions to look into, is that are most webpages have recommended or advertised car links being shown.
  - I ended up just throwing 90% of my scraping program, the 10% I saved was the saving to a the carlist_'city name'.csv
  - I found a new website to scrape from, 'cars.com', it wasn't to bad to scrape from it.
      + I ended up adding a way to scrape from a inputed number of pages, to be on the safe side I'm keeping it at 10 pages for my purposes
      + Found a new way to scrape, my scrap time for 100 cars was less than 3 seconds,
          ~ looks great for first 1,000 cars. I'm going to run a proper collection run in the morning
          
          
July 24, 2020
    -( about 5:30 ) Started my scraping programs for New York, L.A., and Chicago
        + 10 minutes in I had over 10k cars in 10 minutes, regardless of repeats the number of cars being collected will be huge.
    - Using the 10k cars I had I started re-working my data cleaning functions in jupyter notebook
        + finished cleaning functions, I just need to let scrapers run.
    - Scrapers finshed all together in 2-hours, over 640k cars collected.
        + intersting points:
            ~ After running cleaning, and removing duplicates, and any row that has a NUll value.
              I saw had ~11k unique cars, which correlates with the 98% loss I saw in my first run.
              Now I should note, I'm using a 20 mile radius and car.com sorts and shows the cars which are closest to your location first.
    - Ploted some graphs showning the top 10 car manufatures I'm interested for EDA:
        ~ see Github page for graps
    - Hypothesis Testing:
        + does average price of used toyota ~= used mazda with alpha =0.05
          Do a T-test, I didn't have time for power, But I did get a value of 0.06
          So Yes the price of a used mazda = used toyota
        + does average price of a used mercedes-benz ~= used BMW with alpha =0.05
           Do a T-test, I didn't have time for power, But I did get a value of 0.0006..
           So no the price of a used mercedes /= used BMW
            


   
