__author__ = 'Steve'
from webScraper.InitScrape import get_init_scrape

mockInitInfo1 = {
    'statusInfo': {
        'status': u'ok',
        'errorCode': 0
    },
    'results': [
    {
        'state': u'California',
        'abbreviation': u'CA',
        'subarea': u'SF,LA,SouthBay'
    },
    {
        'state': u'Minnesota',
        'abbreviation': u'MN',
        'subarea': u'Minneapolis,Duluth'
    }]
}

mockInitInfo2 = {
    'statusInfo': {
        'status': u'error',
        'errorCode': 400
    },
    'results': []
}

error = {
    'statusInfo': {
        'status': u'error',
        'errorCode': 500
    },
    'results': []
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

