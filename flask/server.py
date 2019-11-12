from __future__ import print_function

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index1', methods=['GET'])
def get_index1():

    return render_template('index1.html')


@app.route('/index2', methods=['GET'])
def get_index2():

    return render_template('index2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')