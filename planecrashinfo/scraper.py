import logging
import requests

logging.basicConfig(filename='scrape.log', level=20)
logging.info('Initialized logger')

def get_page_html(link):
    response = requests.get(link)
    print(response.text)
    return response.text

get_page_html("http://www.planecrashinfo.com/1920/1920.htm")