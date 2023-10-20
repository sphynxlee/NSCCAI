from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'howdy dude!'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/calc/<int:num1>,<int:num2>')
def calc(num1, num2):
    return f'The sum of {num1} and {num2} is %d' % (num1 + num2)

@app.route('/addfunc/<a>,<b>')
def addfunc(a, b):
    return f'The sum of {a} and {b} is %d' % (int(a) + int(b))

@app.route('/inputValue/<val>')
def input_value(val):
    return 'The value is %s' % val

@app.route('/user/<username>,<int:age>')
def show_user_profile(username, age):
    return {"username": username, "age": age}

@app.post('/process_form')
def echo_data():
    the_secret = request.form['secret']
    return the_secret

@app.post('/process_img')
def echo_img():
    the_img = request.files['my_file']
    return the_img.filename