import requests
import urllib
from requests_html import HTMLSession
import csv
import io
import time

data = []
vysledky = []
pole = []
odkazKw = dict
polozka = dict
radek = []

URLs = "URL-2-2023.csv"
KWs = "kw-2-2023.csv"
FILE = "vystupy/2-2023-cz2.csv"


def url_composer():
    with io.open(URLs, "r", encoding="utf8",newline='') as fp:
        for line in fp:
            url = line.lower()
            url = url.strip()
            with io.open(KWs, "r", encoding="utf8",newline='') as gp:
                for line in gp:
                    row = line.strip()
                    row = urllib.parse.quote_plus(row)
                    composedURL = "https://www.google.com/search?q=site%3A" + url + "+" + row + "&ie=UTF-8"
                    odkazKw= {1: composedURL, 2: row}
                    data.append(odkazKw)
        return data
                    
def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
        
def get_results(query):
    
    response = get_source(query)
    print (response)
    time.sleep(30)
   
    
    return response

def parse_results(response):
    
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    
    
    results = response.html.find(css_identifier_result)

    output = []
    
    for result in results:
        item = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href'],
            
        }
        
        output.append(item)
        
    return output

def google_search(query):
    response = get_results(query)
    return parse_results(response)



url_composer()

for dotaz in data:
    result = google_search(dotaz[1])
    kw = dotaz[2]
    if result:
        for vysledek in result:
            odkaz = vysledek['link']
            radek.append((odkaz,kw))
            
      
with open(FILE, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(radek)    