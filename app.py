from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Response Data'

@app.route('/another')
def another_msg():
    return 'Another Response'

@app.route('/test_request/<param>')
def test_request(param):
    return f'test_request:{param}'