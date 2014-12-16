from flask import Flask, render_template, session, request, jsonify, redirect, url_for
from lib import *


app = Flask(__name__)

@app.route('/')
def main(input=None, output=None):
    return render_template('index.html', output=output)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    """Evaluates the input expression and outputs the result."""
    raw_string = request.form['raw_string']
    output = produce_output(raw_string)
    return render_template('index.html', input=raw_string, output=output)

if __name__ == '__main__':
    app.run(debug=True)
