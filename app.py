from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def container():
    return jsonify(message='Hello, welcome to the container API!')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)

    