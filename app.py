from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
import os

from security import authenticate, identity
from resources.item import Item, ItemList
from resources.store import StoreList, Store
from resources.user import UserRegister

app = Flask(__name__)
file_path = os.path.abspath(os.getcwd())+"\data.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)


# this creates /auth end point
jwt = JWT(app, authenticate, identity)


'''
you will have to first call /auth end point, pass user name and password. 
Then you will get jwt token. 
'''


api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/stores/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)


