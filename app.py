from flask import Flask, request, render_template, jsonify

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

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exercise')
def exercise_html():
    return render_template('exercise.html')

@app.route('/answer')
def answer_html():
    return render_template("answer.html", name=request.args.get("my_name"))

@app.route('/try_rest', methods=['POST'])
def try_rest():
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"request_json":request_json}
    return jsonify(response_json)

@app.route('/try_html')
def try_html():
    return render_template('./try_html.html')

@app.route('/show_data', methods=['GET', 'POST'])
def show_data():
    return request.form