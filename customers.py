from flask_restful import Resource, reqparse
from flask import jsonify
import sqlite3

class Customer(Resource):
    TABLE_NAME = 'customers'

    def get(self, cusid):
        item = self.find_by_cusid(cusid)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_cusid(cls, cusid):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE CLIENTNUM =?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (cusid,))
        row = result.fetchone()
        connection.close()


        if row:
            return jsonify(row)
