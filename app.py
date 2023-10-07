from flask import Flask, request, render_template

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
