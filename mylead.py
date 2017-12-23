from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://br18vuhew61fenss:cv8rdgdu9il3foxw@jlg7sfncbhyvga14.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/s6h9a1esmvlviuvp'
db = SQLAlchemy(app)

from baseLeadsApi import *
from dbhelper import * 


if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
    
    