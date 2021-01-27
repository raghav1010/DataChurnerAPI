from flask import Flask
from flask_restful import Api
from resources.customers import Customer
from models.customers import CustomerModel
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SECRET_KEY']='raghabendra'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

api = Api(app)
api.add_resource(Customer, '/customers')
admin =Admin(app)

if __name__ == '__main__':
    from flask_sqlalchemy import SQLAlchemy

    db=SQLAlchemy()
    db.init_app(app)
    admin.add_view(ModelView(CustomerModel,db.session))
    app.run(debug=True)
