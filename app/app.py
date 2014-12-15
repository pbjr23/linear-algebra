from flask import Flask, render_template, session, request, jsonify, redirect, url_for
import matrix
import parser


app = Flask(__name__)

@app.route('/')
def main(output=None):
    return render_template('index.html', output=output)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    """Evaluates the input expression and outputs the result."""
    if request.method == 'POST':
        raw_string = request.form['raw_string']

        stock_info = transactions.get_info(stock_symbol_lookup)
    return render_template('index.html', balance=session['balance'], inventory=session['inventory'], selected=stock_info)

if __name__ == '__main__':
    app.run(debug=True)