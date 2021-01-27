from flask_restful import Resource, reqparse
from flask import jsonify,request,abort
import sqlite3
from models.customers import CustomerModel
import json

def get_paginated_list(results, url, start, limit):
    start = int(start)
    limit = int(limit)
    count = len(results)
    print(results)
    if count < start or limit < 0:
        abort(404)
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['item'] = results[(start - 1):(start - 1 + limit)]
    return obj






class Customer(Resource):
    TABLE_NAME = 'customers'

    def get(self):
        di={}
        x={"CLIENTNUM","Attrition_Flag","Customer_Age","Gender","Dependent_count","Education_Level","Marital_Status","Income_Category","Card_Category","Months_on_book","Total_Relationship_Count","Months_Inactive_12_mon","Contacts_Count_12_mon","Credit_Limit","Total_Revolving_Bal","Avg_Open_To_Buy","Total_Amt_Chng_Q4_Q1","Total_Trans_Amt", "Total_Trans_Ct", "Total_Ct_Chng_Q4_Q1" ,"Avg_Utilization_Ratio" , "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1", "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"}
        if request.args :

            for i in request.args.items():
                if i[0] in x:
                    di[i[0]]=i[1]
                else:
                    return {'message': 'Please enter a valid parameter query'}, 400

        item = CustomerModel.find_by(di)
        j=[]
        if item:
            #print(item)

            for i in item:
                s={}
                s["CLIENTNUM"]=i.CLIENTNUM
                s["Attrition_Flag"]=i.Attrition_Flag
                s["Customer_Age"]=i.Customer_Age
                s["Gender"]=i.Gender
                s["Dependent_count"]=i.Dependent_count
                s["Education_Level"]=i.Education_Level
                s["Marital_Status"]=i.Marital_Status
                s["Income_Category"]=i.Income_Category
                s["Card_Category"]=i.Card_Category
                s["Months_on_book"]=i.Months_on_book
                s["Total_Relationship_Count"]=i.Total_Relationship_Count
                s["Months_Inactive_12_mon"]=i.Months_Inactive_12_mon
                s["Contacts_Count_12_mon"]=i.Contacts_Count_12_mon
                s["Credit_Limit"]=i.Credit_Limit
                s["Total_Revolving_Bal"]=i.Total_Revolving_Bal
                s["Avg_Open_To_Buy"]=i.Avg_Open_To_Buy
                s["Total_Amt_Chng_Q4_Q1"]=i.Total_Amt_Chng_Q4_Q1
                s["Total_Trans_Amt"]=i.Total_Trans_Amt
                s["Total_Trans_Ct"]=i.Total_Trans_Ct
                s["Total_Ct_Chng_Q4_Q1"]=i.Total_Ct_Chng_Q4_Q1
                s["Avg_Utilization_Ratio"]=i.Avg_Utilization_Ratio
                s["Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1"]=i.Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1
                s["Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"]=i.Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2
                j.append(s)
            return jsonify(get_paginated_list(j,request.url,start=request.args.get('start', 1),limit=request.args.get('limit', 20)))
        return {'message': 'Item not found'}, 404
