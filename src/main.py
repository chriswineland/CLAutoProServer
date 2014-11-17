#!flask/bin/python
from flask import Flask, jsonify, make_response
from httpRequestHandler import RequestHandler

app = Flask(__name__)

httpRequestHandler = RequestHandler.RequestHandler()

@app.route('/api/init/<int:mock>', methods=['GET'])
def init(mock):
    global httpRequestHandler
    return jsonify(httpRequestHandler.handle_init(mock))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)