from flask import Flask, jsonify, render_template, request
import json

from flask import jsonify

# https://pymongo.readthedocs.io/en/stable/tutorial.html
# https://matplotlib.org/

def generateToken(user_login):
    return blake2b(b"{user_login}").hexdigest();



def checkTokenValidation(user_login,token):
    return compare_digest(blake2b(b'user_name:qsd,password:123').hexdigest(),res)


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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validation',methods=['GET','POST'])
def getToken():
    user_login = request.form['user_login']
    token = generateToken(user_login)
    resp = make_response(render_template('/list_api'))
    resp.set_cookie('token',token)
    resp.set_cookie('user_login',user_login)
    return html ;


@app.route('/test')
def test():
    f = open('./owid-covid-data.json', 'r')
    datas = json.load(f)

    return render_template('test.html', data=[datas])


@app.route('/api/pays', methods=['GET', 'POST'])
def api():
    f = open('./owid-covid-data.json', 'r')
    datas = json.load(f)

    return jsonify(list(datas.keys()))


# FLASK_ENV="development"
if __name__ == '__main__':
    app.run(debug=True)
