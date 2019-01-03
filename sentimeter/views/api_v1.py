import traceback
import requests
import flask
from flask import jsonify, request, render_template, url_for, Response
from sentimeter import app, logger
from sentimeter.helpers.helpers import decorator_function
from sentimeter.helpers.encryption import get_key, encode_data, decode_data
import assistant.views 

@app.route('/api/v1/test')
def test():
    """
    Testing the Flask Application
    """
    return "It Works!!!"


@app.route('/api/v1/emotion')
def analyze_input():
    try:
        usr_input = request.args.get('input')
        ret_dict = {
            'status': 200,
            'requestLocation': '/api/v1/emotion',
            'input': usr_input,
            'emotion': ''
        }
        return jsonify(ret_dict)
    except Exception as e:
        logger.info(traceback.format_exc())
        return '<h1>Oops, Something unexpected happened.</h1> <br> Team of professionally trained monkeys dispatched for inspection'
