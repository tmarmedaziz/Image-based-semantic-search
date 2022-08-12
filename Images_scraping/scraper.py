import imp
from lib2to3.pgen2 import driver
from sqlite3 import Time
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import pandas as pd

import requests

scrollnum = 10
sleepTimer = 3
chromeDriverPath = r"C:\Users\moham\Image-Based_Semantic_Search\Images_scraping\chromedriver.exe"

# choose the field of interest in scraping 
var = ['drink', 'soda', 'juice', 'drinkable']

profiles = []
image_links = {}


for variable in var:
    url = f'https://www.pinterest.fr/search/pins/?q={variable}'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path=chromeDriverPath, options=options)
    driver.get(url)
    
    for _  in range(1, scrollnum):
        driver.execute_script("window.scrollTo(1,100000)")
        print("scroll down")
        soup = BeautifulSoup(driver.page_source, 'html.parser')


        # find profiles pictures to put them out of the dataset
        listToStr = ' '.join([str(elem) for elem in soup.find_all("div", {"class": "Pj7 sLG XiG INd m1e"})])

        profile_pics = BeautifulSoup(listToStr, 'html.parser')
        for prof in profile_pics.findAll('img'):
            profiles.append(prof['src'])
            # print(prof['src'])


        # extract all images from the page
        for link in soup.findAll('img'):
            image_links[link['src']] = link['alt']
            #print(link['src'])
        
        sleep(sleepTimer)
    print(variable)



# deleting profile pictures from the dict to save them
for item in profiles:
    try:
        del image_links[item]
    except:
        pass


# load data in a json file
with open('profiles_data.json', 'w') as fp:
    json.dump(profiles, fp)


# load data in a csv file
df = pd.DataFrame(list(image_links.items()), columns = ['image_link','images_description'])
df.to_csv('scraped_data.csv')
