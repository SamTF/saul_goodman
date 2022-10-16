### IMPORTS
# Web scraping
from bs4 import BeautifulSoup
import requests

### FETCHING RULING
def fetch_rule(keyword: str) -> str:
    # getting the website source code
    source = requests.get(f'https://mtg.fandom.com/wiki/{keyword}').text

    # creating html parser object
    soup = BeautifulSoup(source, 'lxml')

    # finding the keyword ruling text (if it exists)
    try:
        info_table = soup.find('table')
        row = info_table.find(text='Reminder Text').parent.parent
        ruling = row.find('i').text
        print(ruling)
    # error handling
    except:
        return f'Oopsie! Keyword [{keyword}] was not found :/'

    return ruling[1:-1] # removes the brackets