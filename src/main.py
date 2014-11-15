#!flask/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

initInfo = {
    'statusInfo': {
        'status': u'ok',
        'errorCode': 0
    },
    'results': [
    {
        'state': u'California',
        'abbreviation':u'CA',
        'subarea':u'SF,LA,SouthBay'
    },
    {
        'state': u'Minneosta',
        'abbreviation':u'MN',
        'subarea':u'Minneapolis,Duluth'
    }]
}

@app.route('/api/init', methods=['GET'])
def init():
    return jsonify({'init': initInfo})

if __name__ == '__main__':
    app.run(debug=True)