import requests
from bs4 import BeautifulSoup


def parse_actor_page(link):
    soup = BeautifulSoup(requests.get(link).text)
    
    filmography_list = []

    acting_table_values = soup.select_one('h3.zero')
    full_values = acting_table_values.find_next('table')

    for entry in full_values.select('a.tooltip'):
        filmography_list.append(entry.text)

    filmography_list = list(set(filmography_list))

    return filmography_list    


