import csv , sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_table= "CREATE TABLE IF NOT EXISTS customers (CLIENTNUM INTEGER PRIMARY KEY , Attrition_Flag TEXT , Customer_Age INTEGER, Gender TEXT, Dependent_count INTEGER, Education_Level TEXT, Marital_Status TEXT, Income_Category TEXT, Card_Category TEXT, Months_on_book INTEGER, Total_Relationship_Count INTEGER , Months_Inactive_12_mon INTEGER, Contacts_Count_12_mon INTEGER, Credit_Limit INTEGER , Total_Revolving_Bal INTEGER, Avg_Open_To_Buy INTEGER, Total_Amt_Chng_Q4_Q1 REAL, Total_Trans_Amt INTEGER, Total_Trans_Ct INTEGER, Total_Ct_Chng_Q4_Q1 REAL, Avg_Utilization_Ratio REAL, Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1 REAL, Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2 REAL)"

cursor.execute(create_table)

with open('data.csv','r') as fin:
    dr=csv.DictReader(fin)
    to_db=[( i["CLIENTNUM"] , i["Attrition_Flag"] , i["Customer_Age"] , i["Gender"], i["Dependent_count"] , i["Education_Level"] ,i["Marital_Status"], i["Income_Category"], i["Card_Category"] , i["Months_on_book"] , i["Total_Relationship_Count"] , i["Months_Inactive_12_mon"] , i["Contacts_Count_12_mon"] , i["Credit_Limit"] ,i["Total_Revolving_Bal"] , i["Avg_Open_To_Buy"] , i["Total_Amt_Chng_Q4_Q1"] , i["Total_Trans_Amt"] , i["Total_Trans_Ct"] , i["Total_Ct_Chng_Q4_Q1"] , i["Avg_Utilization_Ratio"] , i["Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1"] , i["Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"]) for i in dr]

cursor.executemany("INSERT INTO customers (CLIENTNUM,Attrition_Flag,Customer_Age,Gender,Dependent_count,Education_Level,Marital_Status,Income_Category,Card_Category,Months_on_book,Total_Relationship_Count,Months_Inactive_12_mon,Contacts_Count_12_mon,Credit_Limit,Total_Revolving_Bal,Avg_Open_To_Buy,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1 , Avg_Utilization_Ratio , Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1, Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db )


connection.commit()
connection.close()
