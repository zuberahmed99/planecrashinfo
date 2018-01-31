import logging
import requests
import cv2
from bs4 import BeautifulSoup

logging.basicConfig(filename='scrape.log', level=20)
logging.info('Initialized logger')

URL = "http://www.planecrashinfo.com/"

def get_page_html(link):
    response = requests.get(link)
    print(response.text)
    return response.text


def get_soup_object(html):
    return BeautifulSoup(html)

def get_table_rows(soup):
    rows = soup.find_all("tr")



def get_data(starting_year, current_year):
    for year in range(starting_year, current_year+1):
        html = get_page_html(URL + str(year) + "/" + str(year) + ".htm")
        soup = get_soup_object(html)


get_data(1998, 2000)
