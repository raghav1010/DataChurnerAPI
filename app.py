from flask import Flask
from flask_restful import Api
from customers import Customer
app = Flask(__name__)
api = Api(app)
api.add_resource(Customer, '/customers/<int:cusid>')

if __name__ == '__main__':
    app.run(debug=True)
