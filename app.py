from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Add/', methods=['POST', 'GET'])
def add():
    num1 = float(request.form.get('number1', 0))
    num2 = float(request.form.get('number2', 0))
    result = num1 + num2
    data = {'result': result}
    data = jsonify(data)
    return data

@app.route('/Sub/', methods=['POST', 'GET'])
def sub():
    num1 = float(request.form.get('number1', 0))
    num2 = float(request.form.get('number2', 0))
    result = num1 - num2
    data = {'result': result}
    data = jsonify(data)
    return data

@app.route('/Mul/', methods=['POST', 'GET'])
def mul():
    num1 = float(request.form.get('number1', 0))
    num2 = float(request.form.get('number2', 0))
    result = num1 * num2
    data = {'result': result}
    data = jsonify(data)
    return data

@app.route('/Div/', methods=['POST', 'GET'])
def div():
    num1 = float(request.form.get('number1', 0))
    num2 = float(request.form.get('number2', 0))
    result = num1 / num2
    data = {'result': result}
    data = jsonify(data)
    return data

if __name__ == '__main__':
    app.run(debug=True)