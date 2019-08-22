from http import HTTPStatus

from flask import Flask, jsonify, request

import nlp

app = Flask(__name__)


def json_error(error, status_code=HTTPStatus.BAD_REQUEST):
    resp = jsonify(error=error)
    resp.status_code = status_code
    return resp


@app.route('/tokenize', methods=['POST'])
def tokenize():
    data = request.get_data()
    if not data:
        return json_error('empty request')

    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError as err:
        return json_error(str(err))

    return jsonify(tokens=nlp.tokenize(text))


@app.route('/health')
def health():
    return jsonify(ok=True)


def main():
    from os import environ

    port = int(environ.get('NLPD_PORT', '8080'))
    app.run(debug='DEBUG' in environ, port=port)


if __name__ == '__main__':
    main()
