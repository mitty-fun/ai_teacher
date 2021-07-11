from flask import Flask, render_template, request
from challenges import challenges

app = Flask(__name__)

judger_py = ''
with open('assets/judger.py', 'r') as file:
    judger_py = file.read()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/judger', methods=['POST'])
def sandbox_judger():
    script = request.form['script']
    inputs = request.form['inputs']
    outputs = request.form['outputs']
    return render_template('sandbox/judger.html', script=script, inputs=inputs, outputs=outputs, data=judger_py)

@app.route('/python/<int:id>')
def python(id):
    data = challenges[id - 1]
    return render_template('python.html', data=data, id=id, challenges=challenges)