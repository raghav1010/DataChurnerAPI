import sqlite3

from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
class CustomerModel(db.Model):
    __tablename__="customers"

    CLIENTNUM= db.Column(db.Integer , primary_key=True)
    Attrition_Flag=db.Column(db.String(200))
    Customer_Age=db.Column(db.Integer)
    Gender=db.Column(db.String(200))
    Dependent_count=db.Column(db.Integer)
    Education_Level=db.Column(db.String(200))
    Marital_Status=db.Column(db.String(200))
    Income_Category=db.Column(db.String(200))
    Card_Category=db.Column(db.String(200))
    Months_on_book=db.Column(db.Integer)
    Total_Relationship_Count=db.Column(db.Integer)
    Months_Inactive_12_mon=db.Column(db.Integer)
    Contacts_Count_12_mon=db.Column(db.Integer)
    Credit_Limit=db.Column(db.Integer)
    Total_Revolving_Bal=db.Column(db.Integer)
    Avg_Open_To_Buy=db.Column(db.Integer)
    Total_Amt_Chng_Q4_Q1=db.Column(db.Float)
    Total_Trans_Amt=db.Column(db.Integer)
    Total_Trans_Ct=db.Column(db.Integer)
    Total_Ct_Chng_Q4_Q1=db.Column(db.Float)
    Avg_Utilization_Ratio=db.Column(db.Float)
    Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1=db.Column(db.Float)
    Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2=db.Column(db.Float)



    def __init__(self,CLIENTNUM,Attrition_Flag,Customer_Age,Gender,Dependent_count,Education_Level,Marital_Status,Income_Category,Card_Category,Months_on_book,Total_Relationship_Count,Months_Inactive_12_mon,Contacts_Count_12_mon,Credit_Limit,Total_Revolving_Bal,Avg_Open_To_Buy,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1 , Avg_Utilization_Ratio , Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1, Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2):

        self.CLIENTNUM=CLIENTNUM
        self.Attrition_Flag=Attrition_Flag
        self.Customer_Age=Customer_Age
        self.Gender=Gender
        self.Dependent_count=Dependent_count
        self.Education_Level=Education_Level
        self.Marital_Status=Marital_Status
        self.Income_Category=Income_Category
        self.Card_Category=Card_Category
        self.Months_on_book=Months_on_book
        self.Total_Relationship_Count=Total_Relationship_Count
        self.Months_Inactive_12_mon=Months_Inactive_12_mon
        self.Contacts_Count_12_mon=Contacts_Count_12_mon
        self.Credit_Limit=Credit_Limit
        self.Total_Revolving_Bal=Total_Revolving_Bal
        self.Avg_Open_To_Buy=Avg_Open_To_Buy
        self.Total_Amt_Chng_Q4_Q1=Total_Amt_Chng_Q4_Q1
        self.Total_Trans_Amt=Total_Trans_Amt
        self.Total_Trans_Ct=Total_Trans_Ct
        self.Total_Ct_Chng_Q4_Q1=Total_Ct_Chng_Q4_Q1
        self.Avg_Utilization_Ratio=Avg_Utilization_Ratio
        self.Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1=Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1
        self.Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2=Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2

    def json(self):
        return {}


    @classmethod
    def find_by(cls,di):
        r= cls.query.filter_by(**di).all()
        return r
