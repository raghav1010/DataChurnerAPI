from flask import Flask
from flask_restful import Api
from resources.customers import Customer



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

api = Api(app)
api.add_resource(Customer, '/customers')


if __name__ == '__main__':
    from flask_sqlalchemy import SQLAlchemy

    db=SQLAlchemy()
    db.init_app(app)
    app.run(debug=True)
