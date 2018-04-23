import logging
import requests
import cv2
from bs4 import BeautifulSoup
import pandas as pd

logging.basicConfig(filename='scrape.log', level=20)
logging.info('Initialized logger')

URL = "http://www.planecrashinfo.com/"
CSV_FILE = "crash_list.csv"


def get_page_html(link):
    response = requests.get(link)
    print(response.text)
    return response.text


def get_soup_object(html):
    return BeautifulSoup(html)

def get_table_rows(soup):
    rows = soup.find_all("tr")
    return rows

def parse_rows(row):
    values = row.findAll("font")
    date = location = aircraft = fatalities= "NA"
    date = values[0].text
    location = values[1].text
    aircraft = values[2].text
    fatalities = values[3].text
    print (location)

def parse_data(soup):
    rows = get_table_rows(soup)
    for row in rows:
        parse_rows(row)
    #print(rows)

def get_data(starting_year, current_year):
    for year in range(starting_year, current_year+1):
        get_year_data(year)

def get_year_data(year):
    html = get_page_html(URL + str(year) + "/" + str(year) + ".htm")
    soup = get_soup_object(html)
    parse_data(soup)


get_data(1998, 2000)
