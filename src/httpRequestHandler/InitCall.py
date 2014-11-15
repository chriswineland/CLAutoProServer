__author__ = 'Steve'

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
        'errorCode': 500
    },
    'results': []
}


class InitCall(object):

    def __init__(self):
        return

    def get_init_data(self, mock_mode):
        if mock_mode == 1:
            global mockInitInfo1
            return mockInitInfo1
        else:
            if mock_mode == 2:
                global mockInitInfo2
                return mockInitInfo2