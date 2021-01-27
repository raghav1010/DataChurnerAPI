from flask_restful import Resource, reqparse
from flask import jsonify,request
import sqlite3

class Customer(Resource):
    TABLE_NAME = 'customers'

    def get(self):
        di={}
        if request.args:
            for i in request.args.items():
                di[i[0]]=i[1]

        item = self.find_by_cusid(di)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_cusid(cls,di):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=cls.TABLE_NAME)
        result = cursor.execute(query)
        row = result.fetchall()
        connection.close()

        d={}
        z=1
        if row:
            for i in range(len(row)):
                s={}
                s["CLIENTNUM"]=str(row[i][0])
                s["Attrition_Flag"]=row[i][1]
                s["Customer_Age"]=str(row[i][2])
                s["Gender"]=row[i][3]
                s["Dependent_count"]=str(row[i][4])
                s["Education_Level"]=row[i][5]
                s["Marital_Status"]=row[i][6]
                s["Income_Category"]=row[i][7]
                s["Card_Category"]=row[i][8]
                s["Months_on_book"]=str(row[i][9])
                s["Total_Relationship_Count"]=str(row[i][10])
                s["Months_Inactive_12_mon"]=str(row[i][11])
                s["Contacts_Count_12_mon"]=str(row[i][12])
                s["Credit_Limit"]=str(row[i][13])
                s["Total_Revolving_Bal"]=str(row[i][14])
                s["Avg_Open_To_Buy"]=str(row[i][15])
                s["Total_Amt_Chng_Q4_Q1"]=str(row[i][16])
                s["Total_Trans_Amt"]=str(row[i][17])
                s["Total_Trans_Ct"]=str(row[i][18])
                s["Total_Ct_Chng_Q4_Q1"]=str(row[i][19])
                s["Avg_Utilization_Ratio"]=str(row[i][20])
                s["Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1"]=str(row[i][21])
                s["Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"]=str(row[i][22])

                res = all(s.get(key,None)==val for key,val in di.items())
                if res==True:
                    d[z]=s
                    z=z+1



        return d
