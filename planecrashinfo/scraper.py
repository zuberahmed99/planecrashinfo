import logging
import requests
import cv2
from bs4 import BeautifulSoup
import pandas as pd
import os

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
    try:
        date = values[0].text
    except Exception as exp:
        pass
    try:
        location = values[1].text
    except Exception as exp:
        pass
    try:
        aircraft = values[2].text
    except Exception as exp:
        pass
    try:
        fatalities = values[3].text
    except Exception as exp:
        pass

    crash_info = {'date': date,
                   'location': location,
                   'aircraft': aircraft,
                   'fatalities': fatalities
                   }

    crash_info_df = pd.DataFrame(crash_info, index=[0])

    # if file does not exist write header
    if not os.path.isfile(CSV_FILE):
        crash_info_df.to_csv(CSV_FILE, header=True, encoding='utf-8')
    else:  # else it exists so append without writing the header
        crash_info_df.to_csv(CSV_FILE, mode='a', header=False, encoding='utf-8')


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
