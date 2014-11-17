__author__ = 'Steve'
from bs4 import BeautifulSoup
import requests

url = 'http://www.craigslist.org/about/sites'


def get_init_scrape():
    global url
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    init_data = {}
    region_data = soup.find_all('h1')
    i = 0
    for region in region_data:
        region_id = 'region' + str(i)
        init_data[region_id] = {}
        abbreviation = region.contents[0]
        init_data[region_id]['region_id'] = abbreviation.get('name')
        init_data[region_id]['region_name'] = region.contents[1]
        subregion_container = region.next_sibling.next_sibling
        all_subregions = subregion_container.find_all('h4')
        y = 0
        for subregion in all_subregions:
            subregion_id = 'subregion' + str(y)
            init_data[region_id][subregion_id] = {}
            subregion_name = subregion.contents[0]
            init_data[region_id][subregion_id]['subregion_name'] = subregion_name
            subdomain_container = subregion.next_sibling.next_sibling
            all_subdomains = subdomain_container.find_all('li')
            z = 0
            for subdomain in all_subdomains:
                subdomain_id = 'subdomain' + str(z)
                init_data[region_id][subregion_id][subdomain_id] = {}
                init_data[region_id][subregion_id][subdomain_id]['subdomain_link'] = subdomain.contents[0].get('href')
                init_data[region_id][subregion_id][subdomain_id]['subdomain_title'] = subdomain.contents[0].contents[0]
                z += 1
            y += 1
        i += 1
    return init_data


print(get_init_scrape())

