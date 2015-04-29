from flask import Flask, render_template, request
from lib import *


app = Flask(__name__)


@app.route('/')
def main(input=None, output=None):
    return render_template('index.html', output=output)


@app.route('/evaluate', methods=['POST'])
def evaluate():
    """Evaluates the input expression and outputs the result."""
    raw_string = request.form.get('raw_string')
    try:
        output = produce_output(raw_string)
    except MatrixException as e:
        output = str(e)
    except Exception as e:
        output = 'Invalid input given!'
    return render_template('index.html', input=raw_string, output=output)

if __name__ == '__main__':
    app.run(debug=True)
