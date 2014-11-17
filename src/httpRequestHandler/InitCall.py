__author__ = 'Steve'
from webScraper.InitScrape import get_init_scrape

mockInitInfo1 = {
    'status_info': {
        'status': "successful",
        'status_code': 200
    },
    'region0': {
        'region_id': "US",
        'region_name': "US",
        'subregion0': {
            'subdomain0': {
                'subdomain_link': "http://auburn.craigslist.org",
                'subdomain_title': "auburn"
            },
            'subdomain1': {
                'subdomain_link': "http://bham.craigslist.org",
                'subdomain_title': "birmingham"
            },
            'subdomain2': {
                'subdomain_link': "http://dothan.craigslist.org",
                'subdomain_title': "dothan"
            },
            'subdomain3': {
                'subdomain_link': "http://shoals.craigslist.org",
                'subdomain_title': "florence / muscle shoals"
            },
            'subdomain4': {
                'subdomain_link': "http://gadsden.craigslist.org",
                'subdomain_title': "gadsden-anniston"
            },
            'subdomain5': {
                'subdomain_link': "http://huntsville.craigslist.org",
                'subdomain_title': "huntsville / decatur"
            },
            'subdomain6': {
                'subdomain_link': "http://mobile.craigslist.org",
                'subdomain_title': "mobile"
            },
            'subdomain7': {
                'subdomain_link': "http://montgomery.craigslist.org",
                'subdomain_title': "montgomery"
            },
            'subdomain8': {
                'subdomain_link': "http://tuscaloosa.craigslist.org",
                'subdomain_title': "tuscaloosa"
            },
            'subregion_name': "Alabama"
        }
    }
}

mockInitInfo2 = {
    'status_info': {
        'status': "error: mock",
        'status_code': 500
    },
    'results': {}
}

error = {
    'status_info': {
        'status': "error: out_of_bounds_mock_value",
        'errorCode': 500
    },
    'results': {}
}


class InitCall(object):

    def __init__(self):
        return

    def get_init_data(self, mock_mode):
        if mock_mode == 0:
            return get_init_scrape()
        if mock_mode == 1:
            global mockInitInfo1
            return mockInitInfo1
        if mock_mode == 2:
            global mockInitInfo2
            return mockInitInfo2
        global error
        return error
