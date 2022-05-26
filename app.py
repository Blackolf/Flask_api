from flask import Flask, jsonify, render_template
from pymongo import MongoClient
import json

from flask import jsonify

# https://pymongo.readthedocs.io/en/stable/tutorial.html
# https://matplotlib.org/

def generateToken(user,password):
    print(f"generate token")


def checkToken(token):
    print(f"check token")


def token_require(func):
    def wrapper(*args,**kwargs):
        print(f"decorator work")
    return wrapper

app = Flask(__name__)


@app.route('/')
# this function return data in a plot format
def main():  # put application's code here
    # create a list of data to pass to the template
    data = [
        {'name': 'Alice', 'age': '25'},
        {'name': 'Bob', 'age': '27'},
        {'name': 'Charlie', 'age': '29'},
    ]
    # render the template with the data
    return render_template('index.html', data=data)


@app.route('/test')
def test():
    f = open('./owid-covid-data.json', 'r')
    datas = json.load(f)
    # for data in datas:
    #     print(data)

    return render_template('test.html', data=[datas])


@app.route('/api/pays', methods=['GET', 'POST'])
def api():
    f = open('./owid-covid-data.json', 'r')
    datas = json.load(f)

    return jsonify(list(datas.keys()))


# FLASK_ENV="development"
if __name__ == '__main__':
    app.run(debug=True)
