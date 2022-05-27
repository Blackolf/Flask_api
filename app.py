from flask import Flask, jsonify, render_template, request , make_response , redirect
from hashlib import blake2b
from hmac import compare_digest
import json

from datetime import datetime

from flask import jsonify

# https://pymongo.readthedocs.io/en/stable/tutorial.html
# https://matplotlib.org/

def generateToken(user_login):
    return blake2b(b"{user_login}").hexdigest();

def log_information(user):
    log_file = open('./logs.log','a+')
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log_file.write(f'INFO - {date} - {user=} - {request.path} \n')
    log_file.close()



def checkTokenValidation(user_login,token):
    return compare_digest(blake2b(b'user_name:qsd,password:123').hexdigest(),token)

def token_verifie(f):
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers

        cki_user_login =request.cookies.get('user_login')
        cki_token =request.cookies.get('token')

        if not cki_token: # throw error if no token provided
            return make_response(jsonify({"message": "A valid token is missing!"}), 401)

        if checkTokenValidation(cki_user_login ,cki_token) == False:
            redirect('/login')
        log_information(cki_user_login)

        return f(*args, **kwargs)
    return decorator



app = Flask(__name__)


# @app.route('/')
# # this function return data in a plot format
# def main():  # put application's code here
#     # create a list of data to pass to the template
#     data = [
#         {'name': 'Alice', 'age': '25'},
#         {'name': 'Bob', 'age': '27'},
#         {'name': 'Charlie', 'age': '29'},
#     ]
#     # render the template with the data
#     return render_template('index.html', data=data)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/validation',methods=['GET','POST'])
def getToken():
    data = dict()
    user_login = request.form['user_login']

    token = generateToken(user_login)
    resp = make_response(render_template('/list_api.html',data=data))
    resp.set_cookie('token',token)
    resp.set_cookie('user_login',user_login)
    data['token'] = token
    data['user_login'] = user_login


    return resp ;


@app.route('/test')
def test():

    cki_user_login =request.cookies.get('user_login')
    cki_token =request.cookies.get('token')

    return f"""
    {cki_user_login}
    {cki_token}
    """


@app.route('/api/pays', methods=['GET', 'POST'])
@token_verifie
def api():
    f = open('./owid-covid-data.json', 'r')
    datas = json.load(f)

    return jsonify(list(datas.keys()))


# FLASK_ENV="development"
if __name__ == '__main__':
    app.run(debug=True)
