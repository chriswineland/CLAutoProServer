#!flask/bin/python
from flask import Flask, jsonify, make_response
from httpRequestHandler import RequestHandler

app = Flask(__name__)

httpRequestHandler = RequestHandler.RequestHandler()

@app.route('/api/init', methods=['GET'])
def init():
    global httpRequestHandler
    return jsonify(httpRequestHandler.handle_init(2))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)